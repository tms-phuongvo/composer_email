import logging
from langchain_openai import ChatOpenAI
from langchain_core.messages import BaseMessage
from src.service.llm.base import BaseService


class OpenAIService(BaseService):

    def __init__(self, **configuration: dict):
        super().__init__()
        self.open_ai = ChatOpenAI(
            **configuration,
        )

    def chatCompletion(self, message: list[BaseMessage]) -> BaseMessage:
        try:
            logging.info("START CALL API")
            response = self.open_ai.invoke(input=message)
            logging.info("DATA: %s", response)
            return response
        except Exception as e:
            raise e
        finally:
            logging.info("END CALL API")
