from pynput.keyboard import KeyCode, Key
import ctypes
from config import *


def get_letter(key: KeyCode):
    if not hasattr(key, 'char'):
        return key

    char = key.char
    return KeyCode.from_char(char)

def get_language():
    user32 = ctypes.windll.LoadLibrary("user32.dll")
    keyboard_state = getattr(user32, "GetKeyboardLayout")
    if hex(keyboard_state(0)) == '0x4090409':
        return 'en'
    return 'ru'

def get_sequnce(lang):
    swap = ru_swap if lang == 'ru' else en_swap
    swap_first_state = ru_swap_first_state if lang == 'ru' else en_swap_first_state
    swap_second_state = ru_swap_second_state if lang == 'ru' else en_swap_second_state
    pa = move + move + swap + move
    pz = move + swap + move + move
    sequences = {
        True: pa,
        False: pz,
        KeyCode.from_char('x'): [move_small, KeyCode.from_char('1'), move_small],
        KeyCode.from_char('ч'): [move_small, KeyCode.from_char('1'), move_small],
        KeyCode.from_char('c'): [move_small, KeyCode.from_char('2'), move_small],
        KeyCode.from_char('с'): [move_small, KeyCode.from_char('2'), move_small],
        KeyCode.from_char('f'): [KeyCode.from_char('v')],
        KeyCode.from_char('а'): [KeyCode.from_char('м')],
    }
    return sequences

