from PIL import Image


def main():
    picture = Image.open("./resources/img2.png")

    picture = Image.new('RGB', (picture.width, picture.height), (0, 0, 0))
