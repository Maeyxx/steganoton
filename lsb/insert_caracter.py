from PIL import Image
from PIL import ImageDraw


def load(original_name):
    """
    Load the picture and store the pixels in a list
    :param original_name: input image name
    :return: the pixels in a list
    """
    pixel_list = []
    # ouverture du fichier image
    pic_in = Image.open(original_name)
    assert isinstance(pic_in, Image.Image)
    for x in range(0, pic_in.width):
        for y in range(0, pic_in.height):
            pixel = pic_in.getpixel((x, y))
            pixel_list.append(pixel)
    return pixel_list, pic_in.width,  pic_in.height


def hide_msg(pixel_list, width, height, new_name):
    new_pixel_list = []
    A = [0, 1, 0, 0, 0, 0, 0, 1]
    lettre = 0
    for original_pixel in pixel_list:
        r = original_pixel[0]
        g = original_pixel[1]
        b = original_pixel[2]
        if lettre < 8:
            r = r + A[lettre]
            bon_pixel = (r, g, b)
            lettre = lettre + 1
        else:
            bon_pixel = (r, g, b)

        new_pixel_list.append(bon_pixel)
    message = export(new_pixel_list, width, height, new_name)
    return message


def decode(pixel_list, width, height, new_name):
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


if __name__ == "__main__":
    # chargement de l'image

    real_pixels_list, width, height = load(
        '../resources/test.jpg')
    decode(real_pixels_list, width,
           height, '../resources/test3.jpg')
