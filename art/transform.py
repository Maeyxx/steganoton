from PIL import Image

from PIL import Image


def loadMage(img):
    picture = Image.open(img)
    px = picture.load()
    picture.close()
    return px, picture.width, picture.height


def copyMage(px, width, height, img, new_img):
    picture2 = Image.new('RGB', (width, height), color='white')
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = px[x, y]
            picture2.putpixel((x, y), (r, g, b))
    picture2.save(new_img)


def contrastMage(px, width, height, img, new_img):
    picture3 = Image.new('RGB', (width, height), color='white')
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = px[x, y]
            picture3.putpixel((x, y), (r ^ 255, g ^ 255, b ^ 255))
    picture3.save(new_img)


def levelGray(px, width, height, img, new_img):
    picture4 = Image.new('RGB', (width, height), color='white')
    for x in range(0, width):
        for y in range(0, height):
            r, g, b = px[x, y]
            grey = int((r + g + b) / 3)
            greyPixel = (grey, grey, grey)
            picture4.putpixel((x, y), (greyPixel))
    picture4.save(new_img)
