#!/usr/bin/env python

from gfxhat import touch, lcd, backlight, fonts
from PIL import Image, ImageFont, ImageDraw


class Display:

    def __init__(self, information):
        self.information = information

    def show(self):
        text= self.information
        width, height = lcd.dimensions()
        image = Image.new('P', (width, height))
        draw = ImageDraw.Draw(image)

        font = ImageFont.load_default()
        w, h = font.getsize(text)

        x = (width - w) // 2
        y = (height - h) // 2

        draw.text((x,y), text, 1, font)
        for x in range(128):
            for y in range(64):
                pixel = image.getpixel((x, y))
                lcd.set_pixel(x, y, pixel)

        lcd.show()

