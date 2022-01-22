from handlers.handler import AbstractHandler
from pynput.keyboard import Key, KeyCode
from utils import aggregate_sequence


class KiteFirst(AbstractHandler):

    _move = [Key.home]
    _chars = aggregate_sequence(['xч'])

    def get_actions(self, action, lang: str):
        if action not in self._chars:
            return super()._to_next_handler(action, lang)
        return self._move + [KeyCode.from_char('1')] + self._move


class KiteSecond(AbstractHandler):

    _move = [Key.home]
    _chars = aggregate_sequence(['cс'])

    def get_actions(self, action, lang: str):
        if action not in self._chars:
            return super()._to_next_handler(action, lang)
        return self._move + [KeyCode.from_char('2')] + self._move


class FastFly(AbstractHandler):

    _move = [Key.home]
    _chars = aggregate_sequence(['fа'])

    def get_actions(self, action, lang: str):
        if action not in self._chars:
            return super()._to_next_handler(action, lang)
        if lang == 'ru':
            return [0.1, KeyCode.from_char('м')]
        if lang == 'en':
            return [0.1, KeyCode.from_char('v')]
        raise NotImplementedError
