#!/usr/bin/env python
import sys
import warnings
import os

from datetime import datetime

from crewai_yepcode_demo.crew import CrewaiYepcodeDemo
from crewai_tools import MCPServerAdapter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew for the asteroid impact scenario with hardcoded inputs.
    """
    inputs = {
        "size": 1000,  # diameter in meters
        "speed": 20,   # speed in km/s
        "angle": 45,   # impact angle in degrees
        "composition": "stony"  # composition type
    }
    try:
        yepcode_token = os.environ.get("YEPCODE_API_TOKEN")
        if not yepcode_token:
            raise EnvironmentError("YEPCODE_API_TOKEN environment variable is not set.")
        server_params = {"url": f"https://cloud.yepcode.io/mcp/{yepcode_token}/sse?mcpOptions=skipRunCodeCleanup"}
        mcp_server_adapter = MCPServerAdapter(server_params)
        with mcp_server_adapter as tools:
            print(f"Available tools from SSE MCP server: {[tool.name for tool in tools]}")
            CrewaiYepcodeDemo(tools=tools).crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CrewaiYepcodeDemo().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewaiYepcodeDemo().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        CrewaiYepcodeDemo().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
