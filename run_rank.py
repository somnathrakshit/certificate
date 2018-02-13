from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv

SEPARATOR = '/'


def resize_image(filename, ratio):
    img = Image.open(filename)
    return img.resize([int(ratio * s) for s in img.size])


if __name__ == "__main__":
    reader = csv.reader(open('rank.csv', 'r'))
    # next(reader, None)
    rows = list(reader)

    bentham = ImageFont.truetype('fonts' + SEPARATOR + 'Bentham.otf', 25)
    cambo = ImageFont.truetype('fonts' + SEPARATOR + 'Cambo-Regular.otf', 25)
    cambo_small = ImageFont.truetype('fonts' + SEPARATOR + 'Cambo-Regular.otf',
                                     18)
    vibes = ImageFont.truetype('fonts' + SEPARATOR + 'GreatVibes-Regular.otf',
                               25)

    sign = resize_image("signs/1.png", 0.4)

    for row in rows:
        img = Image.open("template_rank.png")
        W, H = img.size
        draw = ImageDraw.Draw(img)
        color_black = (0, 0, 0)
        color_brown = (98, 74, 65)

        rank = str(row[0]).strip()
        name = row[1].strip().upper()
        school = row[2].strip().upper()

        w, h = draw.textsize(name, font=cambo)
        draw.text(((W - w) / 2, 400), name, color_black, font=cambo)

        w, h = draw.textsize(school, font=cambo)
        draw.text(((W - w) / 2, 485), school, color_black, font=cambo)

        draw.text((361, 515), rank, color_black, font=cambo_small)

        img.paste((sign), (680, 593), sign)

        filename = 'out' + SEPARATOR + name + '.png'
        img.save(filename, "PNG", quality=100.0)
        print(filename)
        # break
