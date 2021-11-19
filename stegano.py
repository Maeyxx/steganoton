from PIL import Image
from art import transform


def main():
    px, width, height = transform.loadMage('resources/img.jpeg')
    transform.copyMage(px, width, height, 'resources/img.png',
                       'resources/copy.png')
    transform.contrastMage(px, width, height, 'resources/img.png',
                           'resources/contrast.png')
    transform.levelGray(px, width, height, 'resources/img.png',
                        'resources/gris.png')


if __name__ == "__main__":
    main()
