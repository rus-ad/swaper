from pynput import keyboard
import time


class BaseRouter:

    def __init__(
            self
    ):
        self.controller = keyboard.Controller()
        self.time_sleep_pass = 2
        self.time_sleep_release = 2
        self.letter = '1'

    def on_press(self, input_key):
        """..."""
        print(input_key)

    def on_release(self, input_key):
        if input_key == keyboard.Key.menu:
            return False


    def run(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release,
        ) as listener:
            listener.join()


router = BaseRouter()
router.run()

while True:
    time.sleep(router.time_sleep_pass)
    router.controller.press(keyboard.KeyCode.from_char(router.letter))
    time.sleep(router.time_sleep_release)
    router.controller.release(keyboard.KeyCode.from_char(router.letter))

