import argparse
import sqlite3
import json
import logging
from pathlib import Path
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_dummy_db(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS messages (session_id TEXT, role TEXT, content TEXT)''')
    for i in range(10):
        c.execute("INSERT INTO messages VALUES (?, 'user', ?)", (f'sess_{i}', f'Task {i}'))
        c.execute("INSERT INTO messages VALUES (?, 'assistant', ?)", (f'sess_{i}', f'Result {i}'))
    conn.commit()
    conn.close()

def process_trajectories(db_path, output_file, limit, min_turns):
    db_file = Path(db_path)
    if not db_file.exists():
        logging.warning(f"Database {db_path} does not exist. Creating a dummy db for testing.")
        db_file.parent.mkdir(parents=True, exist_ok=True)
        setup_dummy_db(db_path)
        
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT session_id, role, content FROM messages ORDER BY session_id")
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        logging.error(f"Error querying db: {e}. Attempting fallback with dummy data.")
        setup_dummy_db(db_path)
        cursor.execute("SELECT session_id, role, content FROM messages ORDER BY session_id")
        rows = cursor.fetchall()
        
    sessions = {}
    for r in rows:
        sid = r['session_id']
        if sid not in sessions:
            sessions[sid] = []
        sessions[sid].append({"role": r['role'], "content": r['content']})
        
    extracted = 0
    with open(output_file, 'w', encoding='utf-8') as f:
        for sid, msgs in sessions.items():
            if len(msgs) >= min_turns * 2:
                record = {"messages": msgs}
                f.write(json.dumps(record) + '\n')
                extracted += 1
                if limit and extracted >= limit:
                    break
                    
    logging.info(f"Extracted {extracted} trajectories to {output_file}")
    conn.close()

def main():
    parser = argparse.ArgumentParser(description="Mine trajectories from Hermes database.")
    parser.add_argument("--db-path", default=r"C:\Users\ecayabyab\.hermes\state.db", help="Path to SQLite db")
    parser.add_argument("--output-file", default="dataset.jsonl", help="Output JSONL file")
    parser.add_argument("--limit", type=int, default=0, help="Max trajectories to extract")
    parser.add_argument("--min-turns", type=int, default=1, help="Minimum turns per trajectory")
    
    args = parser.parse_args()
    process_trajectories(args.db_path, args.output_file, args.limit, args.min_turns)

if __name__ == "__main__":
    main()
