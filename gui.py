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


class GUI:
    def __init__(self):
        self.apocryphes = []


        # self.commands = {
        #         'print': print(apo),
        #         'quit': None,  # TODO: créer une fonction arret qui modifie un arg global
        #         'reset': apo.reset,  # Oui
        #         'save': apo.save,  # Oui TODO: nommage de la save
        #         'import': None,  # TODO: import via un nom
        #         'sort': apo.sort,  # TODO: facile à faire
        #         'sorta': apo.sort_alphabetical,  # TODO: izi
        #         'squit': apo.s_quit,  # TODO: ridicule, mais je vais le faire
        #         'unlock': apo.unlock,  # TODO: izi
        #         'lock': lethe.lock # TODO: en fait ca c'est eazy mais bon...
        #         }

    def save(self, nickname):
        pass

    def delete(self, nickname):
        pass

    def add(self, filename, nickname):
        pass

    def load(self, nickname):
        pass

    def unload(self, nickname):
        pass

    def branch(self, nickname):
        pass

    def merge(self, target, nickname):
        pass

    def savestate(self):
        pass

    # def init(self):
    #     # INITIALISATION
    #     apo = Apocryphe()
    #     continuation = True
    #     while continuation:
    #         clr_screen(1)
    #         # Séléction du mot
    #         selected_word = apo.select()
    #         print(selected_word)
    #         entry = input(">:")


def construct_filename():
    now = datetime.datetime.now()
    date = now.strftime("_%Y-%m-%d|%H:%M:") + str(now.second)
    return 'usr/apocryphes/apocryphe_' + date + '.pkl'


def clr_screen(i):
    for a in range(i):
        print()

if __name__ == '__main__':
     main = GUI()
     pass
