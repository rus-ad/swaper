from utils import get_letter, get_language, get_sequnce
from config import languages

from pynput import keyboard
from pynput.keyboard import KeyCode
import time


class BaseRouter:

    def __init__(
            self,
            time_sleep_pass: float = 0.01,
            time_sleep_release: float = 0.01,
    ):
        self.time_sleep_pass = time_sleep_pass
        self.time_sleep_release = time_sleep_release
        self.controller = keyboard.Controller()
        self.counter = 0
        self.state = True
        self.magic_state = True
        self.language = get_language()
        self.sequences = get_sequnce(self.language)

    def actions(self, events):
        for event in events:
            #time.sleep(self.time_sleep_pass)
            self.controller.press(event)
            #time.sleep(self.time_sleep_release)
            self.controller.release(event)
        self.counter = len(events) + 1

    def on_press(self, input_key):
        if not self.counter:
            key = get_letter(input_key)
            if key == keyboard.Key.end:
                self.actions(self.sequences[self.state])
                self.state = not self.state

            if key in self.sequences:
                events = self.sequences[input_key]
                if isinstance(events, dict):
                    self.actions(events[self.magic_state])
                    self.magic_state = not self.magic_state
                else:
                    self.actions(events)

            if input_key == keyboard.Key.alt_l:
                self.language = languages[self.language]
                self.sequences = get_sequnce(self.language)

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
            except Exception as e:
                print('{0} was pressed'.format(e.args[0]))


router = BaseRouter()
router.run()
