"""
File: yanzhengma.py
Author: Jin Lexuan
E-mail: jlx321@126.com
Time: 2020-03-25 17:17:36
Function:


"""


from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    return chr(random.randint(65, 90))


def rndColour():
    return random.randint(64, 255), random.randint(64, 255), random.randint(64, 255)


def rndColour2():
    return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)


width = 60*4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('Arial.ttf', 36)
draw = ImageDraw.Draw(image)
for i in range(width):
    for j in range(height):
        draw.point((i, j), fill=rndColour())
for t in range(4):
    draw.text((60*t+10, 10), rndChar(), font=font, fill=rndColour2())

image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')