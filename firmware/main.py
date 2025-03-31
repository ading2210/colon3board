import board
import busio
import digitalio

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.extensions.international import International
from kmk.keys import KC

from adafruit_mcp230xx.mcp23008 import MCP23008

#set up io expander
i2c = busio.I2C(board.SCL1, board.SDA1)
mcp = MCP23008(i2c)
mcp_pins = [mcp.get_pin(i) for i in range(5)]

#set up keyboard
keyboard = KMKKeyboard()
macros = Macros()
keyboard.modules.append(macros)
keyboard.extensions.append(International())

#define row/col pins
COL_PINS = [
  board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, #col0 - col4
  board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, #col5 - col9
  board.GP20, board.GP21, board.GP22, board.GP26, board.GP27, #col10 - col14
  board.GP28, mcp_pins[0], mcp_pins[1], mcp_pins[2], mcp_pins[3], #col15 - col19
  mcp_pins[4], mcp_pins[5] #col20-col21
]
ROW_PINS = [
  board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, #row0-row4
  board.GP5 #row5
]

#setup key matrix
keyboard.matrix = MatrixScanner(
  column_pins = COL_PINS,
  row_pins = ROW_PINS
)

#alias for cleaner key map
_____ = KC.NO

#setup key map
keyboard.keymap = [
  [KC.ESC,  _____,   KC.F1, KC.F2,   KC.F3, KC.F4, _____,  KC.F5, KC.F6, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.11,   KC.F12,   KC.PSCR, KC.SLCK, KC.PAUS, _____,   _____,   _____,   _____  ],
  [KC.GRV,  KC.N1,   KC.N2, KC.N3,   KC.N4, KC.N5, KC.N6,  KC.N7, KC.N8, KC.N9,   KC.N0,   KC.MINS, KC.EQL,  _____,   KC.BSPC,  KC.INS,  KC.HOME, KC.PGUP, KC.NLCK, KC.PSLS, KC.PAST, KC.PMNS],
  [KC.TAB,  _____,   KC.Q,  KC.W,    KC.E,  KC.R,  KC.T,   KC.Y,  KC.U,  KC.I,    KC.O,    KC.P,    KC.LBRC, KC.RBRC, KC.BSLC,  KC.DEL,  KC.END,  KC.PGDN, KC.P7,   KC.P8,   KC.P9,   KC.PPLS],
  [KC.CAPS, _____,   KC.A,  KC.S,    KC.D,  KC.F,  KC.G,   KC.H,  KC.J,  KC.K,    KC.L,    KC.SCLN, KC.QUOT, KC.ENT,  _____,    _____,   _____,   _____,   KC.P4,   KC.P5,   KC.P6,   _____  ],
  [_____,   KC.LSFT, KC.Z,  KC.X,    KC.C,  KC.V,  KC.B,   KC.N,  KC.M,  KC.COMM, KC.DOT,  KC.SLSH, _____,   KC.RSFT, _____,    _____,   KC.UP,   _____,   KC.P1,   KC.P2,   KC.P3,   KC.PENT],
  [KC.LCTL, KC.LWIN, _____, KC.LALT, _____, _____, KC.SPC, _____, _____, _____,   KC.RALT, KC.RWIN, _____,   KC.MENU, KC.RCTL,  KC.LEFT, KC.DOWN, KC.RGHT, KC.P0,   _____,   KC.PDOT, _____  ]
]

if __name__ == "__main__":
  keyboard.go()