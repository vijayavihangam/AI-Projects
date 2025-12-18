# Agentic AI Project

Minimal scaffold for an agentic AI project.

Quickstart

1. Create a Python virtualenv and activate it.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Set your OpenAI API key:

```bash
export OPENAI_API_KEY="sk-..."
```

3. Run the interactive agent:

```bash
python main.py
```

Structure

- `src/agentic/agent.py`: core Agent runtime
- `src/agentic/tools/openai_tool.py`: OpenAI wrapper (uses `openai` package)
- `src/agentic/memory/in_memory.py`: simple in-memory conversation store
- `src/agentic/prompts/default_prompt.txt`: system prompt used by the agent
- `tests/`: basic unit test for the Agent

Notes

- The project expects `OPENAI_API_KEY` to be set in the environment for real API calls.
- Use the tests in `tests/` to validate the basic behavior:

```bash
pytest -q
```

If you'd like, I can add Docker support, CI workflow, or integrate a richer toolset (web search, file tools, browser automation). Tell me which next step you prefer.
