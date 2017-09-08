# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:46:41 2017

@author: Lambyor
"""
# IMPORTATIONS
# TODO comprendre les erreurs d'importations
from LMAO import *    # TODO ENLEVER IMPORTATIONS CIRCULAIRES
from IMO import *    # Gère la séléction et la validité du test et d'autres trucs
import random
import csv
import sys


# VARIABLES GLOBALES
FICHIER = "./dict.txt"
IMPORTATION = "./mots.txt"    # TODO DEGEULASSE, utilisé dans IMO !
AFFICHAGE = False


class Apocryphe:
    def __init__(self):
        self.l = to_lethe_list(FICHIER)
        self.sort()

    def select(self):   # le select est celui en 1er
        chosen_indice = random_pond(self.to_pds())
        if chosen_indice == 0:
            self.l[0].pds = self.l[1].pds-1
        self.inv(0, chosen_indice)   # Inv des indices 0 et chosen_indice
        return self.l[0]

    def delete(self, a, *useless):
        try:
            self.l.remove(self.get_lethe(a))
            return True
        except ValueError:
            return False

    def unlock(self, *useless):
        for e in self.l: 
            if e.pds == 0:
                e.pds = 100
        return True

    def reset(self, *useless):
        for e in self.l:
            e.reset()
        return True

    def save(self, *useless):
        save(self.l)
        return True

    def quit(self, *useless):
        sys.exit()

    def s_quit(self, *useless):
        self.save()
        sys.exit()

    def edit(self, key, value):
        for i in range(len(self.l)):
            if key == self.l[i].en:
                self.l[i].fr = value
                return True
        return False

    def inv(self, i, j):
        t = self.l[i]
        self.l[i] = self.l[j]
        self.l[j] = t

    def to_pds(self): return [int(e.pds) for e in self.l]

    def add(self, a, b):    # A REVOIR
        if a is None or b is None:
            return False
        if not(len(a) >= 3 and len(b) > 0):
            return False
        if len(b[0]) <= 3:
            return False
        if self.get_lethe(a) is None:
            self.l.append(Lethe(a, b))
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
        for e in self.l:
            print(e.en + "," + str(e.fr) + "," + str(e.pds))
        print("")
        return True        

    def sort(self, *useless):
        self.l.sort(key=lambda x: x.pds, reverse=True)
        return True

    def sort_alphabetical(self, *useless):
        self.l.sort(key=lambda x: x.en)
        return True

    def get_lethe(self, a, useless=None):
        for e in self.l:
            if e.en == a:
                return e
        return None

    def no_brothers(self, *useless):    # A vérifier !
        self.sort_alphabetical()
        for i, e in enumerate(self.l[:-1]):
            if e.en == self.l[i+1].en:
                self.l.remove(i+1)
        return True


class Lethe:
    def __init__(self, en, fr, pds=100, gud=0, bad=0, last=False, row=0):
        self.en = en
        self.fr = fr
        self.pds = float(pds)
        self.gud = int(gud)
        self.bad = int(bad)
        self.last = last
        self.row = row

    def add_fr(self, sens):
        self.fr.append(sens)
        self.fr = list(set(self.fr))

    def del_fr(self, sens):
        try:
            self.fr.remove(sens)
            return True
        except ValueError:
            return False

    def add_bad(self, i):
        if self.bad + i >= 20 and self.gud + i >= 2:
            self.add_gud(-1)
        elif self.bad >= 20:
            self.bad = 20
        else:
            self.bad += i

    def add_gud(self, i):
        if self.gud + i >= 20 and self.bad + i >= 2:
            self.add_bad(-1)
        elif self.gud >= 20:
            self.gud = 20
        else:
            self.gud += i

    def add_row(self, b):
        if b and self.last and self.row > -10:
            self.row -= 1
        elif not b and not self.last and self.row < 10:
            self.row += 1
        elif not(b and self.last) and self.row <= 4 and self.row >= -4:
            self.row = 0
        self.last = b
        print(colored("ROW: " + str(self.row) + " ", 'grey', 'on_white', attrs=['bold']))

    def set_pds(self, i):
        self.pds = regulate(i, 5, 200)
        return True

    def reset(self):
        self.pds = 100
        self.row = 0
        self.gud = 0
        self.bad = 0

    def test(self, t):    #LOL C BON
        if(AFFICHAGE): line_print("GUD: " + str(self.gud) + " ")
        if(AFFICHAGE): line_print("BAD: " + str(self.bad) + " ")
        if (levenshtein_list(self.fr, t) <= 3):
            self.add_gud(1)
            self.add_row(True)
            self.set_pds(maxf(self.bad, self.gud, self.row)) #LOL COD DE MERD

            line_print("Pds:" + str(int(self.pds)) + " ", None)
            print(colored("GUD: " + str(self.fr) + " ", 'white', "on_green", attrs=['bold']))
            return True
        else:
            self.add_bad(1)
            self.add_row(False)
            self.set_pds(maxf(self.bad, self.gud, self.row))#LOL COD DE MERD

            line_print("Pds:" + str(int(self.pds)) + " ", None)
            print(colored("BAD: " + str(self.fr) + " ", 'white', "on_red", attrs=['bold']))            
            return False

    def lock(self, *useless):
        self.pds = 0
        return True


def to_lethe_list(f):   # Verified
    with open(f, 'r') as f:
        csv_file = csv.reader(f)
        l = list(csv_file)
    return [Lethe(e[0], e[1].split(';'), e[2], e[3], e[4]) for e in l]


def save(l):    # Csv 1/2
    # TODO faire un VRAI csv
    # Todo utiliser les noms de fichiers de data_processing
    with open(FICHIER, mode='w', encoding='utf8') as f:
        for e in l:
            fr = ""
            for j in e.fr:
                fr += ";"+j
            fr = fr[1:]
            f.write(e.en+","+fr+","+str(e.pds)+","+str(e.gud)+","+str(e.bad)+"\n")


def random_pond(l):    # TODO meilleure description de l'algorithme
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
