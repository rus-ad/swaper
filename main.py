import time

from utils import get_letter, get_layout
from chain import ChainListener

from pynput import keyboard
from pynput.keyboard import Key, KeyCode


swith = True

class BaseRouter:

    def __init__(self):
        self.controller = keyboard.Controller()
        self.extractor = ChainListener()
        self.language = get_layout()
        self.all_trigers = self.extractor.extractor.triggers

    def actions(self, events):
        for event in events:
            if isinstance(event, float):
                time.sleep(event)
                continue
            self.controller.press(event)
            self.controller.release(event)

    def on_press(self, input_key):
        global swith
        if swith and input_key in self.all_trigers:
            swith = False
            key = get_letter(input_key)
            sequence = self.extractor.extract_sequence(key, self.language)
            if sequence is not None:
                self.actions(sequence)
            if input_key == keyboard.Key.alt_l:
                self.language = get_layout()

    def on_release(self, input_key):
        global swith
        swith = True
        if input_key == keyboard.Key.insert:
            return False

    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()

        listener = keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release)
        listener.start()


router = BaseRouter()
router.run()
