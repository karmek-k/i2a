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

    # TODO more pythonic
    for row in array:
        result_row = []

        for pixel in row:
            saturation = sum(pixel)
            result_row.append(char_for_saturation(saturation))

        result.append(''.join(result_row))

    return '\n'.join(result)


image = Image.open('dog.jpg')
print(image_to_ascii(image))
