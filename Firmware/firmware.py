import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanner.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers


keyboard = KMKKeyboard()
encoder_handler = EncoderHandler()
keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)

PINS = [
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP3,
]

encoder_handler.pins = (
    (board.GP2, board.GP1, None),
)

encoder_handler.map = [
    (
        (KC.VOLD, KC.VOLU),
    )
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.A,
        KC.B,
        KC.C,
        KC.D,
        KC.TG(1),
    ],
    [
        KC.E,
        KC.F,
        KC.G,
        KC.H,
        KC.TG(1),
    ],
]

if __name__ == "__main__":
    keyboard.go()