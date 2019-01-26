#!/usr/bin/env python

import time
import sys
import atexit

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw




#display a list of radio station





RadioStation ={
    'radioFG': 'http://www.radiofg.com',
    'voltage': 'http://www.radiovoltage.com'
}

# bouton up and down


class Menu:
    def __init__(self, name, action, option=()):
        self.name = name
        self.action = action
        self.option = option

        self.size = fonts.getsize(name)
        self.width, self.height = self.size



def cleanup():
    backlight.set_all(0,0,0)
    backlight.show()
    lcd.clear()
    lcd.show()



try:

    while True;

except KeyboardInterrupt:
    cleanup()