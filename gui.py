# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:55:09 2017

@author: Octave Chenavas, Roi de Pologne-Austro-Hongrie-Occidentale, Chef de la légion impériale de Dalmatie,
Flèche solaire (quoique ca veuille dire)
"""
# from pycallgraph.output import GraphvizOutput   # TODO: vérifier les importations
# from pycallgraph import PyCallGraph
# from termcolor import colored
from apocryphe import *


def clr_screen(i):
    for a in range(i): 
        print()


def main():
    # INITIALISATION
    apo = Apocryphe()
    continuation = True
    while continuation:
        clr_screen(1)
        # Séléction du mot
        selected_word = apo.select()
        print(selected_word)
        entry = input(">:")


def command(texte, apo, lethe):    # CA J'AIME ! OUI J'AIME CA ! OH OUI ! ANNNNNHH !
    liste = texte.split(' ')
    clef = liste[0][1:]
    reste = None
    try:
        reste = liste[1]
        base = reste.split(',')[0]
    except Exception:
        base = None
    try:
        acide = reste.split(',')[1].split(';') 
    except Exception:
        acide = None

    commands = {
        'print': print(apo),
        'quit': None,  # TODO: créer une fonction arret qui modifie un arg global
        'reset': apo.reset,  # Oui
        'save': apo.save,  # Oui TODO: nommage de la save
        'import': None,  # TODO: import via un nom
        'sort': apo.sort,  # TODO: facile à faire
        'sorta': apo.sort_alphabetical,  # TODO: izi
        'squit': apo.s_quit,  # TODO: ridicule, mais je vais le faire
        'unlock': apo.unlock,  # TODO: izi
        'lock': lethe.lock # TODO: en fait ca c'est eazy mais bon...
        }


if __name__ == '__main__':
     main()
     pass
