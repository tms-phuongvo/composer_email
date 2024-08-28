from langchain_core.messages import BaseMessage


class BaseService:
    def chatCompletion(self, message: BaseMessage | list[BaseMessage]) -> BaseMessage:
        raise NotImplementedError
