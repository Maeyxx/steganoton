"""
Author : françois foyer
course : BSI 2021_2022

objectifs : 

    - structurer un programme en packages / modules / fonctions
    - utiliser des packages existants : manipulation d'images numériques
    - créer des fonctions, utiliser des paramètres, retourner des valeurs

"""
from PIL import Image


def load(original_name):
    """
    Load the picture and store the pixels in a list
    :param original_name: input image name
    :return: the pixels in a list
    """
    pixel_list = []
    # ouverture du fichier image
    pic_in = Image.open(original_name)
    for x in range(0, pic_in.width):
        for y in range(0, pic_in.height):
            pixel = pic_in.getpixel((x, y))
            pixel_list.append(pixel)
    return pixel_list, pic_in.width,  pic_in.height


def export(pixel_list, width, height, new_name):
    """
    create a picture and store a pixel list in this picture
    :param pixel_list: pixels to write to the new picture
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    pic_out = Image.new("RGB", (width, height), (0, 0, 0))
    for num_column in range(0, len(pixel_list) // height):
        start = num_column * height
        stop = start + height
        column = pixel_list[start: stop]
        for num_line in range(len(column)):
            pic_out.putpixel((num_column, num_line), tuple(column[num_line]))
    pic_out.save(new_name)
    return f"{new_name} exported successfully."


def transform_gray_scale(pixel_list, width, height, new_name):
    """
    transform to gray scale with an average method
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    gray_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        average = (r + g + b) // 3
        new_gray_pixel = (average, average, average)
        gray_pixels_list.append(new_gray_pixel)
    message = export(gray_pixels_list, width, height, new_name)
    return message


def transform_black(pixel_list, width, height, new_name):
    """
    transform to black
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    new_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        new_pix = (0, 0, 0)
        if r > g:
            new_pix = (255, g, b)
        elif b > r:
            new_pix = (r, g, 255)
        elif g > r:
            new_pix = (r, 255, b)
        new_pixels_list.append(new_pix)
    message = export(new_pixels_list, width, height, new_name)
    return message


def transform_yellow(pixel_list, width, height, new_name):
    """
    transform to yellow
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    new_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        new_pix = (0, 0, 0)
        if r > g:
            new_pix = (0, g, b)
        elif b > r:
            new_pix = (r, g, 0)
        elif g > r:
            new_pix = (r, 0, b)
        new_pixels_list.append(new_pix)
    message = export(new_pixels_list, width, height, new_name)
    return message


def transform_green(pixel_list, width, height, new_name):
    """
    transform to green
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    new_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        new_pix = (0, 0, 0)
        if r < g:
            new_pix = (0, 255, 0)
        elif b < r:
            new_pix = (0, 255, 0)
        elif g < r:
            new_pix = (0, 255, 0)
        new_pixels_list.append(new_pix)
    message = export(new_pixels_list, width, height, new_name)
    return message


def transform_multicolor(pixel_list, width, height, new_name):
    """
    transform to multicolor
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    new_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        new_pix = (255, 255, 255)
        if r > g:
            new_pix = (255, 0, 0)
        elif b > r:
            new_pix = (0, 255, 0)
        elif g > r:
            new_pix = (0, 0, 255)
        new_pixels_list.append(new_pix)
    message = export(new_pixels_list, width, height, new_name)
    return message


def transform_blue(pixel_list, width, height, new_name):
    """
    transform to blue
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :return: something to print
    """
    new_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        new_pix = (255, 255, 255)
        if r > g:
            new_pix = (0, 0, 255)
        elif b > r:
            new_pix = (0, 255, 0)
        elif g > r:
            new_pix = (255, 0, 0)
        new_pixels_list.append(new_pix)
    message = export(new_pixels_list, width, height, new_name)
    return message


def transform_gray_except_one_channel(pixel_list, width, height, new_name, channel):
    """
    transform to gray scale with an average method but keep red values
    :param pixel_list: original image pixels list
    :param width: width of the output picture
    :param height: height of the output picture
    :param new_name: filename of the generated picture
    :param channel: the channel that don't need to be modified
    :return: something to print
    """
    gray_pixels_list = []
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        average = (r + g + b) // 3
        if channel in [0, "r", "R", "red", "rouge"]:
            new_gray_pixel = (r, average, average)
        elif channel in [1, "g", "G", "green", "vert"]:
            new_gray_pixel = (average, g, average)
        elif channel in [2, "b", "B", "blue", "bleu"]:
            new_gray_pixel = (average, average, b)
        else:
            new_gray_pixel = original_pixel
        gray_pixels_list.append(new_gray_pixel)
    message = export(gray_pixels_list, width, height, new_name)
    return message


if __name__ == "__main__":
    # chargement de l'image
    real_pixels_list, width, height = load(
        './resources/08_LaSalleStegano_art.jpg')

    # # copie de l'image
    # print(export(real_pixels_list, width, height, 'copie.png'))

    # # niveau de gris
    # print(transform_gray_scale(real_pixels_list, width, height, 'gris.png'))

    print(transform_black(real_pixels_list, width,
          height, './resources/black.png'))
    print(transform_yellow(real_pixels_list, width,
          height, './resources/yellow.png'))
    print(transform_green(real_pixels_list, width,
          height, './resources/green.png'))
    print(transform_multicolor(real_pixels_list, width,
          height, './resources/multicolor.png'))
    print(transform_blue(real_pixels_list, width, height, './resources/blue.png'))

    # # niveau de gris partiels
    # print(transform_gray_except_one_channel(
    #     real_pixels_list, width, height, 'gris-r.png', "r"))
    # print(transform_gray_except_one_channel(
    #     real_pixels_list, width, height, 'gris-g.png', "g"))
    # print(transform_gray_except_one_channel(
    #     real_pixels_list, width, height, 'gris-b.png', "b"))
