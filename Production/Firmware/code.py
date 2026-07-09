print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D4,board.D5)
keyboard.row_pins = (board.GP1,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.A,KC.B, KC.NO, KC.NO],
    [KC.C,KC.D, KC.NO, KC.NO]
]

if __name__ == '__main__':
    keyboard.go()