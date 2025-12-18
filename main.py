import os
from pathlib import Path

from agentic.agent import Agent
from agentic.tools.openai_tool import OpenAITool
from agentic.memory.in_memory import InMemoryMemory


def main():
    prompt_path = Path("src/agentic/prompts/default_prompt.txt")
    system_prompt = "You are a helpful assistant." 
    if prompt_path.exists():
        try:
            system_prompt = prompt_path.read_text(encoding="utf-8")
        except Exception:
            pass

    try:
        tool = OpenAITool()
    except RuntimeError as e:
        print("Warning:", e)
        print("Interactive mode will still work for dry-run tests (no calls).")
        raise

    mem = InMemoryMemory()
    agent = Agent(tool=tool, memory=mem, system_prompt=system_prompt)
    agent.run_interactive()


if __name__ == "__main__":
    main()
