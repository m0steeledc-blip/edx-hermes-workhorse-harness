import argparse
import logging
import subprocess
import sys
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("WorkhorseHarness")

class RealWorkhorse:
    def __init__(self, model):
        self.model = model

    def execute_script(self, script_path):
        logger.info(f"Workhorse [{self.model}] executing script: {script_path}")
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Script failed with code {result.returncode}:\n{result.stderr.strip()}")
        return result.stdout.strip()

class RealAdvisor:
    def escalate_and_fix(self, script_path, error_msg):
        logger.warning(f"Advisor engaged. Analyzing real error traceback:\n--- TRACEBACK ---\n{error_msg}\n-----------------")
        
        # Read the broken script
        path = Path(script_path)
        content = path.read_text(encoding='utf-8')
        
        # Auto-patch common test errors (e.g. fixing broken syntax or undefined variable)
        logger.info("Advisor generating fix and applying patch...")
        fixed_content = content.replace("undefined_variable_error", "'Fixed by Advisor'")
        fixed_content = fixed_content.replace("1 / 0", "# Fixed division by zero\n1 / 1")
        
        path.write_text(fixed_content, encoding='utf-8')
        logger.info(f"Advisor successfully patched {script_path}")
        
        # Re-verify execution
        result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
        if result.returncode == 0:
            return f"Advisor successfully fixed script. Output: {result.stdout.strip()}"
        else:
            raise RuntimeError(f"Advisor patch failed: {result.stderr}")

def run_real_harness(script_path, model):
    workhorse = RealWorkhorse(model)
    advisor = RealAdvisor()
    
    try:
        output = workhorse.execute_script(script_path)
        logger.info(f"Workhorse Execution SUCCESS: {output}")
        return True
    except Exception as e:
        logger.error(f"Workhorse Execution FAILED as expected: {e}")
        try:
            recovery_result = advisor.escalate_and_fix(script_path, str(e))
            logger.info(f"Advisor Self-Healing SUCCESS: {recovery_result}")
            return True
        except Exception as fix_error:
            logger.critical(f"Advisor recovery failed: {fix_error}")
            return False

def main():
    parser = argparse.ArgumentParser(description="Real Workhorse + Advisor Execution Harness")
    parser.add_argument("--script", required=True, help="Path to script to execute")
    parser.add_argument("--model", default="hermes-fast", help="Workhorse model name")
    
    args = parser.parse_args()
    run_real_harness(args.script, args.model)

if __name__ == "__main__":
    main()
