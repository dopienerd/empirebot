#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont

size = 128
img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Rounded rectangle background
draw.rounded_rectangle([4, 4, 124, 124], radius=20, fill='#e94560')

# White slide shape in center
draw.rounded_rectangle([24, 28, 104, 88], radius=6, fill='#FFFFFF')

# Play triangle on the slide
draw.polygon([(52, 42), (52, 74), (84, 58)], fill='#e94560')

# "PPT" text at bottom
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
except:
    font = ImageFont.load_default()
draw.text((64, 100), "PPT", fill='#FFFFFF', font=font, anchor='mm')

img.save('/home/user/empirebot/presenter_icon.png')
print("Icon created!")
