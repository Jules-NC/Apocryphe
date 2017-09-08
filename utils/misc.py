# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 01:40:32 2017

@author: Lambyor
CC LEVENSTHEIN TO WIKIPEDIA ALGORITHM

Ah oui j'ai voulu mettre des tests mais en fait c'est chiant alors si vous voulez modifier bah bonne chance. 
"""
from apocryphe_core import *
import numpy as np
import math


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


if __name__ == '__main__':

    import_file(True)    # True si oui #Tautologie
    pass
