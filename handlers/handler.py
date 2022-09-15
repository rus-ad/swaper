from pynput.keyboard import Key, KeyCode

from abc import ABC, abstractmethod
from typing import Any

from config import ru_by_eng_letters


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def get_actions(self, action, lang: str):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def __init__(self, move, sequnce: list, trigger):
        self.move = move
        self.sequnce = sequnce
        self.trigger = trigger
        self.ru_chars = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    def get_actions(self, action, lang: str):
        raise NotImplementedError

    def _to_next_handler(self, action: Any, lang: str) -> str:
        if self._next_handler:
            return self._next_handler.get_actions(action, lang)
        return None

    def mapping_for_letters(self, lang: str, chars: str):
        if not isinstance(chars, str):
            return chars
        if lang == 'ru':
            if self.ru_chars is None:
                self.ru_chars = [ru_by_eng_letters[char] for char in chars]
            return [KeyCode.from_char(char) for char in self.ru_chars]
        if lang == 'en':
            return [KeyCode.from_char(char) for char in chars]
        raise NotImplementedError

    def aggregate_sequence(
        self,
        group_chars: list,
        lang: str,
    ) -> list:
        sequence = []
        for chars in group_chars:
            chars = self.mapping_for_letters(lang, chars)
            sequence.extend(chars)
        return sequence
