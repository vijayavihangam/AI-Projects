from typing import List, Dict

class Agent:
    """Simple agent runtime: composes messages, calls a tool, stores memory."""

    def __init__(self, tool, memory, system_prompt: str = None):
        self.tool = tool
        self.memory = memory
        self.system_prompt = system_prompt or "You are a helpful assistant."

    def _build_messages(self, user_input: str) -> List[Dict]:
        messages = []
        messages.append({"role": "system", "content": self.system_prompt})
        messages.extend(self.memory.get_messages())
        messages.append({"role": "user", "content": user_input})
        return messages

    def run_once(self, user_input: str) -> str:
        messages = self._build_messages(user_input)
        resp_text = self.tool.chat(messages)
        # store into memory
        self.memory.add_user(user_input)
        self.memory.add_assistant(resp_text)
        return resp_text

    def run_interactive(self):
        print("Agent interactive mode. Type 'exit' to quit.")
        while True:
            try:
                user_input = input("You: ")
            except (KeyboardInterrupt, EOFError):
                print()
                break
            if not user_input:
                continue
            if user_input.strip().lower() in ("exit", "quit"):
                break
            resp = self.run_once(user_input)
            print("Assistant:", resp)
