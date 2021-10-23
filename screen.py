#!/usr/bin/env python3


from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import yaml


i2c = busio.I2C(SCL, SDA)
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)


padding = -1
top = padding
bottom = height - padding
x = 0
font_small = ImageFont.load_default()
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf", 17)

with open("res.yaml") as re:
    data = yaml.load(re)

i = 0
draw.text(
    (x, top + i),
    str(data["Evolution"] + " | " + data["Date"]),
    font=font_small,
    fill=255,
)
draw.text((x, top + i + 15), str(data["Price"]), font=font, fill=255)

disp.image(image)
disp.show()
