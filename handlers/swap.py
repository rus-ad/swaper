from handlers.handler import AbstractHandler
from pynput.keyboard import Key, KeyCode
from utils import aggregate_sequence


class SwapHandler(AbstractHandler):

    _static_keys = [Key.f1, Key.f2, Key.f3]
    _state = True
    _move = [Key.end]

    def aggregate_command(self, sequence):
        command = self._move.copy()
        if self._state:
            command += self._move + self._move + sequence
        else:
            command += self._move + sequence + self._move
        self._state = not self._state
        command += self._move
        return command

    def get_actions(self, action, lang: str):
        if action != Key.shift_r:
            return super()._to_next_handler(action, lang)

        if lang == 'ru':
            sequence = aggregate_sequence(
                ['98яй', self._static_keys, 'ма'],
            )
            return self.aggregate_command(sequence)
        if lang == 'en':
            sequence = aggregate_sequence(
                ['98zq', self._static_keys, 'vf'],
            )
            return self.aggregate_command(sequence)
        raise NotImplementedError
