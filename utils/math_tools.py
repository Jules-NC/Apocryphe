# -*- coding: utf-8 -*-
import math

def gauss(x, y, s, maximum=100, x0=0, y0=0, sx=1.0, sy=1.0):
    # Oui des librairies font ca très bien
    # ...
    # ...
    # ...
    # MAIS J'AI PAS LE TEMPS
    # Mot-Dièse MADLAB !
    return maximum * math.exp(-((x - x0) ** 2 / (2 * sx ** 2) + (y - y0) ** 2 / (2 * sy ** 2))) + 8.3 * s


def maxf(x, y, s):
    return max(gauss(x, y, s, 100, 0, 0, 3.6, 1.9),
               gauss(x, y, s, 100, 10, 0, 4.5, 3.75),
               gauss(x, y, s, 100, 20, 0, 6.4, 7.8))

