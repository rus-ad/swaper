from pynput.keyboard import KeyCode, Key

import ctypes


def aggregate_sequence(group_chars: list) -> list:
    sequence = []
    for chars in group_chars:
        if isinstance(chars, str):
            chars = [KeyCode.from_char(char) for char in chars]
        sequence.extend(chars)
    return sequence


def get_letter(key: KeyCode):
    if not hasattr(key, 'char'):
        return key
    char = key.char
    return KeyCode.from_char(char)


def get_layout():
    u = ctypes.windll.LoadLibrary("user32.dll")
    pf = getattr(u, "GetKeyboardLayout")
    if hex(pf(0)) == '0x4190419':
        return 'ru'
    if hex(pf(0)) == '0x8090809':
        return 'en'
    raise Exception(f"This type unavalible: {hex(pf(0))}")
