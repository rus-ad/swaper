from handlers.swap import SwapHandler
from handlers.fast_abilities import KiteFirst, KiteSecond, FastFly


class Chain:

    def __init__(self, handlers):
        handler = handlers[0]
        for curr_handler in handlers[1:]:
            handler = handler.set_next(curr_handler)
        self.handler = handlers[0]

    def get_sequence(self, action, lang):
        return self.handler.get_actions(action, lang)


class ChainListener:

    def __init__(self):
        self.extractor = Chain([
            SwapHandler(),
            KiteFirst(),
            KiteSecond(),
            FastFly(),
        ])

    def extract_sequence(self, action, lang):
        return self.extractor.get_sequence(action, lang)
