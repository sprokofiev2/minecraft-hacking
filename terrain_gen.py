from noise import noise2, noise3
from random import random
from settings import *


@njit
def get_height(x, z):
    # amplitude
    a1 = CENTER_Y
    # fractional brownian motion
    a2, a4, a8 = a1 * 0.5, a1 * 0.25, a1 * 0.128

    # frequency
    f1 = 0.005
    f2, f4, f8 = f1 * 2, f1 * 4, f1 * 8

    height = 0
    height += noise2(x * f1, z * f1) * a1 + a1
    height += noise2(x * f2, z * f2) * a2 - a2
    height += noise2(x * f4, z * f4) * a4 + a4
    height += noise2(x * f8, z * f8) * a8 - a8

    height = max(height, 1)

    return int(height)