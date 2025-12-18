import os
import openai
from typing import List, Dict


class OpenAITool:
    """Simple wrapper around the `openai` package for chat completions.

    Requires `OPENAI_API_KEY` in the environment.
    """

    def __init__(self, model: str = "gpt-4o-mini", temperature: float = 0.2):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable is not set")
        openai.api_key = api_key
        self.model = model
        self.temperature = temperature

    def chat(self, messages: List[Dict]) -> str:
        # messages: list of {role: "system|user|assistant", content: str}
        resp = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
        )
        # extract text
        choices = resp.get("choices") or []
        if not choices:
            return ""
        return choices[0]["message"]["content"].strip()
