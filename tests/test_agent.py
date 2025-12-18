import unittest
from agentic.agent import Agent


class DummyTool:
    def __init__(self):
        self.called = False

    def chat(self, messages):
        self.called = True
        return "ok"


class DummyMemory:
    def __init__(self):
        self._msgs = []

    def add_user(self, text):
        self._msgs.append({"role":"user","content":text})

    def add_assistant(self, text):
        self._msgs.append({"role":"assistant","content":text})

    def get_messages(self):
        return list(self._msgs)


class AgentTest(unittest.TestCase):
    def test_run_once_calls_tool_and_stores_memory(self):
        tool = DummyTool()
        mem = DummyMemory()
        a = Agent(tool=tool, memory=mem, system_prompt="sys")
        out = a.run_once("hello")
        self.assertEqual(out, "ok")
        self.assertTrue(tool.called)
        msgs = mem.get_messages()
        self.assertEqual(len(msgs), 2)


if __name__ == '__main__':
    unittest.main()
