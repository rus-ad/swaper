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
    _state = True

    def get_actions(self, action, lang: str):
        if action not in self._chars:
            return super()._to_next_handler(action, lang)
        if self._state:
            self._state = not self._state
            if lang == 'ru':
                return [1.0, KeyCode.from_char('м')]
            if lang == 'en':
                return [1.0, KeyCode.from_char('v')]
        else:
            self._state = not self._state
            return None
        raise NotImplementedError
