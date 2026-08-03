import argparse
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("WorkhorseHarness")

class Workhorse:
    def __init__(self, model):
        self.model = model
        
    def dispatch(self, prompt):
        logger.info(f"Dispatching prompt to {self.model}: {prompt[:50]}...")
        # Simulate execution
        time.sleep(1)
        if "error" in prompt.lower() or "fail" in prompt.lower():
            raise RuntimeError("Tool execution failed during reasoning step.")
        return {"status": "success", "response": "Task completed successfully."}

class Advisor:
    def escalate(self, prompt, error):
        logger.warning(f"Escalating to Advisor. Error traceback: {error}")
        return {"status": "recovered", "response": f"Advisor resolved error: {error}"}

def run_harness(prompt, model):
    workhorse = Workhorse(model)
    advisor = Advisor()
    
    try:
        result = workhorse.dispatch(prompt)
        logger.info(f"Workhorse succeeded: {result['response']}")
    except Exception as e:
        logger.error(f"Workhorse failed: {e}")
        recovery = advisor.escalate(prompt, str(e))
        logger.info(f"Advisor recovery result: {recovery['response']}")

def main():
    parser = argparse.ArgumentParser(description="Workhorse + Advisor Execution Harness")
    parser.add_argument("--prompt", required=True, help="Task prompt to execute")
    parser.add_argument("--model", default="hermes-fast", help="Workhorse model name")
    
    args = parser.parse_args()
    run_harness(args.prompt, args.model)

if __name__ == "__main__":
    main()
