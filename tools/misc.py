# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 01:40:32 2017

@author: Lambyor
CC LEVENSTHEIN TO WIKIPEDIA ALGORITHM

Ah oui j'ai voulu mettre des tests mais en fait c'est chiant alors si vous voulez modifier bah bonne chance. 
"""
import numpy as np
import datetime    # For file name ==> no duplicates
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


def levenshtein_list(l, tg):
    try:
        return min([levenshtein(e, tg) for e in l])
    except ValueError:
        return 100


def regulate(value, min_value, max_value):    # TODO descritption
    # Assert est très très très utile la !
    assert min_value < max_value
    if value <= min_value:
        value = min_value
    elif value >= max_value:
        value = max_value
    assert value >= min_value
    assert value <= max_value
    return value


def import_file(ca_sert_a_quoi_ce_parametre_wtf=False):    # UN PEU DE LA MERDE, RIEN NE VAUT UN HUMAIN
    # TODO COMPRENDRE A QUOI CA SERT !
    if not ca_sert_a_quoi_ce_parametre_wtf:
        return
    with open(IMPORTATION, mode='r', encoding='utf8') as f:
        csv_file = csv.reader(f)
        l = list(csv_file)
    with open(FICHIER, mode='r', encoding='utf8'):
        for e in l:
            if not ca_sert_a_quoi_ce_parametre_wtf:
                break
            print((e[0] + "," + str(e[1]) + ",100,0,0"))


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


def construct_filename(folder='saves', filename='dummy', extension='pkl'):
    now = datetime.datetime.now()
    folder = 'usr/' + folder + '/'
    date = now.strftime("_%Y-%m-%d|%H:%M:") + str(now.second)
    filename = folder + filename + date + '.' + extension
    return filename


if __name__ == '__main__':

    import_file(True)    # True si oui #Tautologie
    pass
