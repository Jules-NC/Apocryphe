# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:46:41 2017

@author: Lambyor
"""
# IMPORTATIONS
# TODO: emplacement des fichiers
from utils.word_analysis import levenshtein_list    # Gère la séléction et la validité du test et d'autres trucs
from utils.math_tools import maxf   # permet de set la valeur de pds
from utils.misc import *     # Limite la valeur de x entre a et b
import random
import csv
import sys


# VARIABLES GLOBALES
FICHIER = "./ressources/dict.txt"
IMPORTATION = "./ressources/mots.txt"
AFFICHAGE = False   # You can visualize bad and gud number of each lethe in LMAO with this


class Apocryphe:
    """It's just a List of Lethes but with a name and some methods

    All the functions with *useless or unused parameters are for a wierd thing, for a call in LMAO.
    I will change this. Because it's 'dégeulasse'
    """
    def __init__(self):
        self.lethe_list = to_lethe_list(FICHIER)
        self.sort()

    def select(self):   # le select est celui en 1er
        """Return the first element in sef.lethe_list after a random

        The random is done withe the random_pond function, ponderate with the pds
        """
        chosen_indice = random_pond(self.to_pds())
        if chosen_indice == 0:
            self.lethe_list[0].pds = self.lethe_list[1].pds - 1
        self.inv(0, chosen_indice)   # Inv des indices 0 et chosen_indice
        return self.lethe_list[0]

    def delete(self, a, *useless):
        try:
            self.lethe_list.remove(self.get_lethe(a))
            return True
        except ValueError:
            return False

    def unlock(self, *useless):
        for e in self.lethe_list:
            if e.pds == 0:
                e.pds = 100
        return True

    def reset(self, *useless):
        for e in self.lethe_list:
            e.reset()
        return True

    def save(self, *useless):
        save(self.lethe_list)
        return True

    def quit(self, *useless):
        sys.exit()

    def s_quit(self, *useless):
        self.save()
        sys.exit()

    def edit(self, key, value):
        for i in range(len(self.lethe_list)):
            if key == self.lethe_list[i].en:
                self.lethe_list[i].fr = value
                return True
        return False

    def inv(self, i, j):
        t = self.lethe_list[i]
        self.lethe_list[i] = self.lethe_list[j]
        self.lethe_list[j] = t

    def to_pds(self): return [int(e.pds) for e in self.lethe_list]

    def add(self, a, b):    # A REVOIR
        if a is None or b is None:
            return False
        if not(len(a) >= 3 and len(b) > 0):
            return False
        if len(b[0]) <= 3:
            return False
        if self.get_lethe(a) is None:
            self.lethe_list.append(Lethe(a, b))
            return True
        return False

    def add_sens(self, a, b):
        if a is None or b is None:
            return False
        if len(a) == 0 or len(b) == 0:
            return False
        mot = self.get_lethe(a)
        if mot is None:    # TODO améliorer ca
            return False
        for e in b:
            mot.add_fr(e)
        return True

    def del_sens(self, a, b):
        if a is None or b is None:
            return False
        if len(a) <= 3 or len(b) == 0:
            return False
        mot = self.get_lethe(a)
        res = False
        for e in b:
            a = mot.del_fr(e)
            if a:
                res = True
        return res

    def sorted_print(self, *useless):
        for e in self.lethe_list:
            print(e.en + "," + str(e.fr) + "," + str(e.pds))
        print("")
        return True        

    def sort(self, *useless):
        self.lethe_list.sort(key=lambda x: x.pds, reverse=True)
        return True

    def sort_alphabetical(self, *useless):
        self.lethe_list.sort(key=lambda x: x.en)
        return True

    def get_lethe(self, a, useless=None):
        for e in self.lethe_list:
            if e.en == a:
                return e
        return None

    def no_brothers(self, *useless):    # A vérifier !
        self.sort_alphabetical()
        for i, e in enumerate(self.lethe_list[:-1]):
            if e.en == self.lethe_list[i+1].en:
                self.lethe_list.remove(i + 1)
        return True


class Lethe:
    """Lethe manages a unique word, and all the parameters associates to theses words.

    Lethe contain many arguments:
    :arg en: The english word
    :arg fr: The french traduction(s) of the word. It's a list
    :arg pds: A value set by gaussian calculations
    :arg gud: Number of test failures
    :arg bad: Number of test success
    :arg row: Number of row fail or success
    """
    def __init__(self, en, fr, pds=100, gud=0, bad=0, last=False, row=0):
        self.en = en
        self.fr = fr
        self.pds = float(pds)
        self.gud = int(gud)
        self.bad = int(bad)
        self.last = last
        self.row = row

    def add_fr(self, meaning):
        """Add a french meaning at the object.

        :param self: Lethe object
        :param meaning: a new meaning of the word
        """
        self.fr.append(meaning)
        self.fr = list(set(self.fr))

    def del_fr(self, meaning):
        """Delete a french meaning at the object.

        :param self: Lethe object
        :param meaning: a meaning of the word to be deleted
        :return: False if meaning is not in self.fr, True otherwise
        """
        try:
            self.fr.remove(meaning)
            return True
        except ValueError:
            return False

    def add_bad(self, i):
        """Regulation of the number of self.bad and self.gud

        A Lethe can't have more than 20 gud or 20 bad (20 included).
        So if a Lethe have more than 20 gud, we reduce the number of bad.
        """
        if self.bad + i >= 20 and self.gud + i >= 2:
            self.add_gud(-1)
        elif self.bad >= 20:
            self.bad = 20
        else:
            self.bad += i

    def add_gud(self, i):
        """Regulation of the number of self.gud and self.bad

        A Lethe can't have more than 20 gud or 20 bad (20 included).
        So if a Lethe have more than 20 gud, we reduce the number of bad.
        """
        if self.gud + i >= 20 and self.bad + i >= 2:
            self.add_bad(-1)
        elif self.gud >= 20:
            self.gud = 20
        else:
            self.gud += i

    def add_row(self, value_to_add):
        """Manages row

        Row set to 0 if True and False and row > 8  (8 is a hyperparameter)
        Row - if True and True
        Row + if False and false
        """
        if value_to_add and self.last and self.row > -10:
            self.row -= 1
        elif not value_to_add and not self.last and self.row < 10:
            self.row += 1
        elif not(value_to_add and self.last) and self.row <= 4 and self.row >= -4:
            self.row = 0
        self.last = value_to_add
        print("ROW: " + str(self.row))

    def set_pds(self, i):
        """Set pds between 5 and 200 included

        :arg i: value you want for self.pds
        :return: i but normalised between 5 and 200
        """
        self.pds = regulate(i, 5, 200)
        return True

    def reset(self):
        """Reset this Lethe to defaults values for all train values"""
        self.pds = 100
        self.row = 0
        self.gud = 0
        self.bad = 0

    def test(self, t):    #LOL C BON
        if(AFFICHAGE): print("GUD: " + str(self.gud))
        if(AFFICHAGE): print("BAD: " + str(self.bad))
        if (levenshtein_list(self.fr, t) <= 3):
            self.add_gud(1)
            self.add_row(True)
            self.set_pds(maxf(self.bad, self.gud, self.row)) #LOL COD DE MERD

            print("Pds:" + str(int(self.pds)))
            print("GUD: " + str(self.fr))
            return True
        else:
            self.add_bad(1)
            self.add_row(False)
            self.set_pds(maxf(self.bad, self.gud, self.row))#LOL COD DE MERD

            print("Pds:" + str(int(self.pds)))
            print("BAD: " + str(self.fr))
            return False

    def lock(self, *useless):
        """Set pds of this Lethe to 0 => will not be selectionned again"""
        self.pds = 0
        return True


def to_lethe_list(f):   # Verified
    """Return a list of all Lethes presents in a pseudo-csv file.

    A pseudo-csv file is a csv file wihout the firts line. It's weird
    So you read this and you create Lethes (1 line = 1 Lethe) and you pack these Lethes together.

    :arg f: the path to the file
    :return A beautiful list of all Lethes presents in your file
    """
    with open(f, 'r') as f:
        csv_file = csv.reader(f)
        l = list(csv_file)
    return [Lethe(e[0], e[1].split(';'), e[2], e[3], e[4]) for e in l]


def save(l):    # Csv 1/2
    # TODO: Bien tout comprendre de si c'est une letheList ou des Lethes on sait pas trop comment
    # TODO: faire un VRAI csv
    # TODO: utiliser les noms de fichiers de data_processing
    with open(FICHIER, mode='w', encoding='utf8') as f:
        for e in l:
            fr = ""
            for j in e.fr:
                fr += ";"+j
            fr = fr[1:]
            f.write(e.en+","+fr+","+str(e.pds)+","+str(e.gud)+","+str(e.bad)+"\n")


def random_pond(l):    # TODO meilleure description de lethe_list'algorithme
    # TODO: Description de cette focntion
    # Init
    chosen_number = random.randint(0, sum(l)-1)
    i = 0
    # Continuation
    while chosen_number > 0:
        chosen_number -= l[i]
        i += 1
    # End
    return i-1

if __name__ == '__main__':
    
    a = Apocryphe()
    a.save()
    
    print("PRINT--")
    a.sorted_print()
    print("SORT--")
    a.sort()
    print("SAVE--")
    a.save()
    print("INV--")
    a.inv(1, 1)
    print("PRINT--")
    a.sorted_print()
    print("TO_LIST--")
    b = a.to_pds()
    print(b)
    print("LEN_B: " + str(len(b)))
    res = [0 for a in range(len(b))]
    for c in range(10000):
        r = random_pond(b)
        res[r] += 1
    print("LEN_RES: " + str(len(res)))
    print(res)
    print("EDIT--")
    a.edit("scabbard", ["bite"])
    a.sorted_print()
    print("ADD--")
    a.add("yes", ['oui', 'pourquoi pas', 'allez!', 'soyez pas vaches les mecs ?'])
    a.sorted_print()
    print(a.get_lethe('wide'))
    print(a.get_lethe('scabbard'))
