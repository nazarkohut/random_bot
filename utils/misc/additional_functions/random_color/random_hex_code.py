import numpy as np


def random_hex_code():
    color = lambda: np.random.randint(0, 255)
    return '%02X%02X%02X' % (color(), color(), color())
