import time

from utils import get_letter, get_layout
from chain import ChainListener

from pynput import keyboard


class BaseRouter:

    def __init__(self):
        self.controller = keyboard.Controller()
        self.extractor = ChainListener()
        self.language = get_layout()
        self.counter = 0

    def actions(self, events):
        for event in events:
            if isinstance(event, float):
                time.sleep(event)
                continue
            self.controller.press(event)
            self.controller.release(event)
        self.counter = len([
            event
            for event in events
            if not isinstance(event, float)
        ])

    def on_press(self, input_key):
        if not self.counter:
            key = get_letter(input_key)
            sequence = self.extractor.extract_sequence(key, self.language)
            if sequence is not None:
                self.actions(sequence)
            if input_key == keyboard.Key.alt_l:
                self.language = get_layout()

    def on_release(self, input_key):
        self.counter -= 1
        if self.counter < 0:
            self.counter = 0
        print(input_key, self.counter)
        if input_key == keyboard.Key.insert:
            return False

    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release,
                suppress=False,
        ) as listener:
            try:
                listener.join()
            except Exception as err_text:
                print(err_text.args[0])


router = BaseRouter()
router.run()
