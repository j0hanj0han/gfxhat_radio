from gfxhat import touch, lcd, backlight, fonts
from  PIL import Image, ImageFont, ImageDraw


class Display():

    def __init__(self, information):
        self.information = information


    def run:
        width, height = lcd.dimensions()

        print(width, height)

        image = Image.new('P', (width, height))
        print(image)

        draw = ImageDraw.Draw(image)

        font = ImageFont.load_default()

        text = "bonjour johan"

        w, h = font.getsize(text)

        x = (width - w) // 2
        y = (height - h) // 2

        draw.text((x, y), text, 1, font)


    def clean:
        pass

