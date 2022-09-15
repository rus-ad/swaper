from handlers.swap import SwapHandler
from config import swap_args


class Chain:
    triggers = []

    def __init__(self, handlers):
        handler = handlers[0]
        self.triggers.append(handler.trigger)
        for curr_handler in handlers[1:]:
            handler = handler.set_next(curr_handler)
            self.triggers.append(handler.trigger)
        self.handler = handlers[0]

    def get_sequence(self, action, lang):
        return self.handler.get_actions(action, lang)


class ChainListener:

    def __init__(self):
        self.extractor = Chain([
            SwapHandler(**swap_args),
        ])

    def extract_sequence(self, action, lang):
        return self.extractor.get_sequence(action, lang)
