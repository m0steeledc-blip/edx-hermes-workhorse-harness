import argparse
import subprocess
import sys
import logging
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

def run_script(script_path):
    logging.info(f"Invoking {script_path}...")
    try:
        subprocess.run([sys.executable, script_path], check=True, capture_output=True, text=True)
        logging.info(f"Successfully ran {script_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {script_path}:\n{e.stderr}")
        raise

def aggregate_datasets(output_file, input_files):
    logging.info(f"Aggregating datasets into {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for infile in input_files:
            in_path = Path(infile)
            if in_path.exists():
                logging.info(f"Reading from {infile}")
                with open(infile, 'r', encoding='utf-8') as f:
                    for line in f:
                        outfile.write(line)
            else:
                logging.warning(f"File not found: {infile}, skipping.")
    logging.info("Aggregation complete.")

def main():
    parser = argparse.ArgumentParser(description="EOD Trajectory Sync Script")
    parser.add_argument('--force', action='store_true', help='Force sync even if not 5 PM')
    args = parser.parse_args()

    # Time check for 5 PM
    now = datetime.now()
    if not args.force and now.hour != 17:
        logging.warning("It is not 5:00 PM (17:00). Use --force to run anyway. Exiting.")
        return

    hermes_dir = Path(r"C:\Users\ecayabyab\.hermes")
    scripts_dir = hermes_dir / "scripts"
    mine_trajectories_script = scripts_dir / "mine_trajectories.py"
    mine_eo_invariants_script = scripts_dir / "mine_eo_invariants.py"
    
    # Run mining scripts
    if mine_eo_invariants_script.exists():
        run_script(str(mine_eo_invariants_script))
    else:
        logging.error(f"{mine_eo_invariants_script} not found!")

    if mine_trajectories_script.exists():
        run_script(str(mine_trajectories_script))
    else:
        logging.warning(f"{mine_trajectories_script} not found! Skipping.")

    # Aggregate
    final_dataset = hermes_dir / "dataset.jsonl"
    invariants_dataset = hermes_dir / "eo_invariants_dataset.jsonl"
    
    inputs = [str(invariants_dataset)]
    trajectories_dataset = hermes_dir / "trajectories.jsonl"
    inputs.append(str(trajectories_dataset))

    aggregate_datasets(str(final_dataset), inputs)

    logging.info(f"Dataset prepared at {final_dataset} for HPUSH mesh sync to VPS / RIG DROP.")

if __name__ == "__main__":
    main()
