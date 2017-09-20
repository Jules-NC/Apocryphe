# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:55:09 2017

@author: Octave Chenavas, Roi de Pologne-Austro-Hongrie-Occidentale, Chef de la légion impériale de Dalmatie,
Flèche solaire (quoique ca veuille dire)
"""
# from pycallgraph.output import GraphvizOutput   # TODO: vérifier les importations
# from pycallgraph import PyCallGraph
from collections import namedtuple
# from termcolor import colored
from apocryphe import *


CONTINUATION = True


def main():
    try:  # If more than first time
        with open('usr/core_savestate.pkl', 'rb') as f:
            gui = pickle.load(f)
    except FileNotFoundError:  # If first time
        gui = GUI()

    gui.main()  # Begin the main process


class GUI:
    def __init__(self):
        self.apocryphes = {'main':Apocryphe()}
        self.files_nicknames = {'main':construct_filename()}
        self.current_branch = 'main'
        self.loaded_apos = ['main']

    def save(self, nickname):
        with open(self.files_nicknames[nickname], 'wb') as f:
            pickle.dump(self.apocryphes[nickname])

    def delete(self, nickname):
        self.unload(nickname)
        del self.files_nicknames[nickname]

    def add(self, filename, nickname):
        try:
            with open(filename, 'r') as f:  # If the file exists
                self.files_nicknames[nickname] = filename
        except FileNotFoundError:
            print('ERREUR: Robinson_Crusoé')

    def load(self, nickname):
        with open(self.files_nicknames[nickname], 'rb') as f:
            self.apocryphes[nickname] = pickle.load(f)
            self.loaded_apos += nickname

    def unload(self, nickname):
        if self.current_branch == nickname:
            self.current_branch = None
        self.loaded_apos.remove(nickname)
        del self.apocryphes[nickname]

    def branch(self, nickname):
        if nickname in self.loaded_apos:
            self.current_branch = nickname
        else:
            print('ERREUR: Nelson_Mandella')

    def merge(self, target, nickname):  # TODO: ca
        pass

    def savestate(self):
        with open('usr/core_savestate.pkl', 'wb') as f:
            pickle.dump(self, f)

    def main(self):
        # apo = self.apocryphes[self.current_branch]
        commands = {
                'delete': self.delete,
                'add': self.add,
                'load': self.load,
                'unload': self.unload,
                'branch': self.branch,
                'merge': self.merge,
                'savestate': self.savestate,
                'quit': continuation_off,
                'train': self.train
                }

        while CONTINUATION:
            entry = command_parser(input('>: '))
            if entry.root in commands:
                try:
                    commands[entry.root](*entry.args)
                except TypeError:
                    print('ERREUR: Jacquouille_la_Fripouille')

    def train(self):
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


Command = namedtuple('Command', ['root', 'args'])


def command_parser(entry):
    entry = entry.split(' ')
    if len(entry[0]) is 0:
        return Command(None, [None])
    return Command(entry[0], entry[1:])


def construct_filename():
    now = datetime.datetime.now()
    date = now.strftime("_%Y-%m-%d|%H:%M:") + str(now.second)
    return 'usr/apocryphes/apo_' + date + '.pkl'


def continuation_off():
    global CONTINUATION
    CONTINUATION = False


def clr_screen(i):
    for a in range(i):
        print()

if __name__ == '__main__':
     main()
     pass
