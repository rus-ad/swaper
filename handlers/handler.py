from abc import ABC, abstractmethod
from typing import Any


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def get_actions(self, action, lang: str):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def get_actions(self, action, lang: str):
        raise NotImplementedError

    def _to_next_handler(self, action: Any, lang: str) -> str:
        if self._next_handler:
            return self._next_handler.get_actions(action, lang)
        return None
