import os
from langchain_anthropic import AnthropicLLM
from langchain_core.messages import BaseMessage
from src.service.llm.base import BaseService


class AnthropicService(BaseService):
    def __init__(self, **configuration: dict):
        self.anthropic = AnthropicLLM(
            **configuration,
        )

    def chatCompletion(self, message: list[BaseMessage]) -> str:
        response = self.anthropic.invoke(input=message)
        return response
