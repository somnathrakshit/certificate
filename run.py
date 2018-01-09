from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv

SEPARATOR = '/'

def resize_image(filename, ratio):
    img = Image.open(filename)
    return img.resize([int(ratio * s) for s in img.size])

if __name__ == "__main__":
    reader = csv.reader(open('data.csv', 'r'))
    next(reader, None)
    rows = list(reader)

    bentham = ImageFont.truetype('fonts' + SEPARATOR + 'Bentham.otf', 25)
    cambo = ImageFont.truetype('fonts' + SEPARATOR + 'Cambo-Regular.otf', 25)
    vibes = ImageFont.truetype('fonts' + SEPARATOR + 'GreatVibes-Regular.otf', 25)

    sign = resize_image("signs/1.png", 0.4)

    for row in rows:
        img = Image.open("template.png")
        W, H = img.size
        draw = ImageDraw.Draw(img)
        color_black = (0, 0, 0)


        name=row[2].strip().upper()
        school=row[4].strip().upper()

        w, h = draw.textsize(name, font=cambo)
        draw.text(((W - w) / 2, 400), name, color_black, font=cambo)

        w, h = draw.textsize(school, font=cambo)
        draw.text(((W - w) / 2, 485), school, color_black, font=cambo)

        img.paste((sign), (680, 593), sign)

        filename = 'out' + SEPARATOR + name + '.png'
        img.save(filename, "PNG", quality=100.0)
        print(filename)
        # break
