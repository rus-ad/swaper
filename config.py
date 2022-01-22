from pynput.keyboard import KeyCode, Key

ru = "йцукенгшщзхъфывапролджэячсмитьбю."
en = "qwertyuiop[]asdfghjkl;'zxcvbnm,./"

languages = {
    'ru': 'en',
    'en': 'ru',
}

move = [Key.end]
move_small = Key.home
ru_swap = [KeyCode.from_char(l) for l in '98яй'] + [Key.f1, Key.f2, Key.f3] + [KeyCode.from_char(l) for l in 'ма']
en_swap = [KeyCode.from_char(l) for l in '98zq'] + [Key.f1, Key.f2, Key.f3] + [KeyCode.from_char(l) for l in 'vf']
swap_letter = '\\'

ru_swap_first_state = KeyCode.from_char('у')
en_swap_first_state = KeyCode.from_char('e')
ru_swap_second_state = KeyCode.from_char("ё")
en_swap_second_state = KeyCode.from_char("'")
