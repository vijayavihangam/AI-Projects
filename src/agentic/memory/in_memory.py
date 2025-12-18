from typing import List, Dict

class InMemoryMemory:
    """Very small in-memory conversation store."""

    def __init__(self, max_items: int = 100):
        self._messages: List[Dict] = []
        self.max_items = max_items

    def add_user(self, text: str):
        self._messages.append({"role": "user", "content": text})
        self._trim()

    def add_assistant(self, text: str):
        self._messages.append({"role": "assistant", "content": text})
        self._trim()

    def get_messages(self) -> List[Dict]:
        return list(self._messages)

    def clear(self):
        self._messages = []

    def _trim(self):
        if len(self._messages) > self.max_items:
            self._messages = self._messages[-self.max_items:]
