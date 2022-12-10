import numpy as np
from PIL import Image


def char_for_saturation(saturation: int):
    # TODO remove constants
    if saturation <= 100:
        return ' '
    elif saturation <= 255:
        return '.'
    elif saturation <= 255 + 255 + 100:
        return '*'
    else:
        return 'W'


def image_to_ascii(img: Image) -> str:
    array = np.asarray(img)

    result = []

    for row in array:
        result_row = [char_for_saturation(sum(pixel)) for pixel in row]

        result.append(''.join(result_row))

    return '\n'.join(result)


image = Image.open('dog.jpg')
print(image_to_ascii(image))
