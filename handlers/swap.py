from handlers.handler import AbstractHandler


class SwapHandler(AbstractHandler):

    _state = True

    def aggregate_command(self, sequence):
        command = self.move.copy()
        if self._state:
            command += self.move + sequence
        else:
            command += sequence + self.move
        self._state = not self._state
        command += self.move
        return command

    def get_actions(self, action, lang: str):
        if action != self.trigger:
            return super()._to_next_handler(action, lang)
        sequence = self.aggregate_sequence(self.sequnce, lang)
        return self.aggregate_command(sequence)
