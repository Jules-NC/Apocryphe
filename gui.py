# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:55:09 2017

@author: Jules Neghnagh--Chenavas, Roi de Pologne-Austro-Hongrie-Occidentale, Chef de la légion impériale de Dalmatie,
Flèche solaire (quoique ca veuille dure)
"""
from pycallgraph.output import GraphvizOutput   # TODO vérifier les importations
from pycallgraph import PyCallGraph
from termcolor import colored
from apocryphe import *


def clr_screen(i):
    for a in range(i): 
        print()


def sys_print():
    pass
    #print(colored("======[" + titre.upper() + "]======", 'white', back, attrs=['bold', 'underline']))


def main():
    # INITIALISATION
    apo = Apocryphe()
    continuation = True
    while continuation:
        clr_screen(1)
        # Séléction du mot
        lethe = apo.select()
        print(colored(' ' + lethe.en + ' ', 'white', 'on_cyan', attrs=['bold']))
        e = input(">:")
        if e == "":
            e = " "
        if e[0] != '/':
            lethe.test(e)
        else:
            command(e, apo, lethe)


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
        'print': apo.sorted_print,
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

    erreurs = {
        'add': ('AddError: truc qui va pas', 'entre clef/val et ; entre valeurs'),
        'del': ('DEL: erreur 404', 'élément non trouvé => non supprimé'),
        'addS': ('AddSens Erreur', 'mot non trouvé'),
        'delS': ('DelSens Erreur', 'sens ou mot non trouvé')
        }
    try:
        a = commands.get(clef)(base, acide)
        # sys_print("AHAH",str(base) +'|'+str(acide), True)
    except TypeError:
        sys_print("commande non trouvée",
                  "Tapez /help pour une liste des commandes",
                  False)
        a = None
    if not a:
        sys_print(erreurs.get(clef)[0], erreurs.get(clef)[1], False)
    else:
        sys_print(clef, 'Opération réussie')

if __name__ == '__main__':
    print(colored('hello', 'cyan', 'on_blue'), colored('world', 'cyan', 'on_red'))
    with PyCallGraph(output=GraphvizOutput()):
        main()
    pass
