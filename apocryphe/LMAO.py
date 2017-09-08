# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 22:55:09 2017

@author: Jules Neghnagh--Chenavas, Roi de Pologne-Austro-Hongrie-Occidentale, Chef de la légion impériale de Dalmatie, Flèche solaire (quoique ca veuille dure)
"""

from ROLF import *
from termcolor import colored

from pycallgraph import PyCallGraph
from pycallgraph.output import GraphvizOutput

def clrScreen(i): 
    for a in range(i): 
        print()

def sys_print(titre, contenu, a=True):
    clrScreen(1)
    if(a == True): color = 'green'; back = 'on_cyan'
    else: color = 'red'; back = 'on_red'
    print(colored("======[" + titre.upper() + "]======", 'white', back, attrs=['bold', 'underline']))
    print(colored(contenu, color))

def line_print(contenu, a = None):   # TODO renommer ca bien (faire att a ROLF qui en utilise beaucoup)
    if(a == True): color = 'white'; back = 'on_green'
    elif (a == False): color = 'white'; back = 'on_red'
    else: color = 'white'; back = 'on_grey'
    print(colored(contenu, color, back, attrs=['bold']))


def main():
    #INITIALISATION
    apo = Apocryphe()
    while(True):
        clrScreen(1)
        #Séléction du mot
        lethe = apo.select()
        print(colored(' ' + lethe.en + ' ', 'white', 'on_cyan', attrs=['bold']))
        e = input(">:")
        if e == "": e = " "
        if(e[0] != '/'): lethe.test(e)
        else: command(e, apo, lethe)


def command(texte, apo, lethe): #CA J'AIME ! OUI J'AIME CA ! OH OUI ! ANNNNNHH !
    liste = texte.split(' ')
    clef = liste[0][1:]

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
        'add':apo.add,
        'addS':apo.add_sens,
        'del':apo.delete,
        'delS':apo.del_sens,
        'print':apo.sorted_print,
        'quit':apo.quit,
        'reset':apo.reset,
        'save':apo.save,
        'sort':apo.sort,
        'sorta':apo.sort_alphabetical,
        'squit':apo.s_quit,
        'unlock':apo.unlock,
        'lock': lethe.lock
        }

    erreurs = {
        'add':('AddError: truc qui va pas',
                ', entre clef/val et ; entre valeurs'),
        'del':('DEL: erreur 404',
               'élément non trouvé => non supprimé'),
        'addS':('AddSens Erreur',
                'mot non trouvé'),
        'delS':('DelSens Erreur',
                'sens ou mot non trouvé')
        }
    try:
        a = commands.get(clef)(base, acide)
        #sys_print("AHAH",str(base) +'|'+str(acide), True)
    except TypeError:
        sys_print("commande non trouvée",
                  "Tapez /help pour une liste des commandes",
                  False)
        a = None
    if a == False:
        sys_print(erreurs.get(clef)[0], erreurs.get(clef)[1], False)
    elif a == True:
        sys_print(clef, 'Opération réussie')

if __name__ == '__main__':
    print(colored('hello', 'cyan','on_blue'), colored('world', 'cyan','on_red'))
    with PyCallGraph(output=GraphvizOutput()):
        main()
    pass