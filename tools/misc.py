# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 01:40:32 2017

@author: Lambyor
CC LEVENSTHEIN TO WIKIPEDIA ALGORITHM

Ah oui j'ai voulu mettre des tests mais en fait c'est chiant alors si vous voulez modifier bah bonne chance. 
"""
import numpy as np
import math


def levenshtein(source, tg):    # UTSUKUSHI DESU DESU MOTTO MOTTO NOTICE ME SEMPAI
    if len(source) < len(tg):
        return levenshtein(tg, source)
    if len(tg) == 0:
        return len(source)
    source = np.array(tuple(source))
    tg = np.array(tuple(tg))
    p_r = np.arange(tg.size + 1)
    for s in source:
        c_r = p_r + 1
        c_r[1:] = np.minimum(c_r[1:], np.add(p_r[:-1], tg != s))
        c_r[1:] = np.minimum(c_r[1:], c_r[0:-1] + 1)
        p_r = c_r
    return p_r[-1]


def min_levenshtein_list(entry, list_of_words):
    minimum = 4242  # Minimum must be at least FENCE + 1 if you want a true powered thing
    for item in list_of_words:
        dist = levenshtein(entry, item)
        if dist < minimum:
            minimum = dist
    return minimum


def gauss_3d(x, y, s, maximum=100, x0=0, y0=0, sx=1.0, sy=1.0):
    return maximum * math.exp(-((x - x0) ** 2 / (2 * sx ** 2) + (y - y0) ** 2 / (2 * sy ** 2))) + 8.3 * s


def space_shape(x, y, s):
    return max(gauss_3d(x, y, s, 100, 0, 0, 3.6, 1.9),
               gauss_3d(x, y, s, 100, 10, 0, 4.5, 3.75),
               gauss_3d(x, y, s, 100, 20, 0, 6.4, 7.8), 5)


if __name__ == '__main__':
    mots = ['lol', 'lel', 'ptdr']
    mot = 'lol'
    print(min_levenshtein_list(mot, mots))
    pass

