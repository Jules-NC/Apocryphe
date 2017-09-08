# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 20:46:41 2017

@author: Lambyor
"""
#IMPORTATIONS
import csv
import sys
import random
from IMO import * #Gère la séléction et la validité du test et d'autres trucs
from termcolor import colored
from LMAO import linePrint

#VARIABLES GLOBALES
FICHIER = "./dict.txt"
IMPORTATION = "./mots.txt"
AFFICHAGE = False

class Apocryphe:
    def __init__(self):
        self.l = toLetheList(FICHIER)
        self.sort()       
    def select(self): #le select est celui en 1er
        r = randomPond(self.toPds())
        if(r == 0):
            self.l[0].pds = self.l[1].pds-1
        self.inv(0,r) #Inv des indices 0 et r
        return self.l[0]
    def delete(self, a, *useless):
        try:
            self.l.remove(self.getLethe(a))
            return True
        except ValueError:
            return False
    def unlock(self, *useless): 
        for e in self.l: 
            if e.pds == 0: e.pds = 100  
        return True 
    def reset(self, *useless):
        for e in self.l:
            e.reset()
        return True
    def save(self, *useless): save(self.l); return True
    def quit(self, *useless): sys.exit()
    def sQuit(self, *useless): self.save(); sys.exit()
    def edit(self, key, value):
        for i in range(len(self.l)):
            if (key == self.l[i].en):
                self.l[i].fr = value
                return True
        return False
    def inv(self, i, j): t = self.l[i]; self.l[i] = self.l[j]; self.l[j] = t
    def toPds(self): return [int(e.pds) for e in self.l]
    def add(self, a, b): # A REVOIR
        if(a == None or b == None): return False
        if(not(len(a)>= 3 and len(b)>0)): return False
        if(len(b[0]) <= 3): return False
        if self.getLethe(a) == None:
            self.l.append(Lethe(a, b))
            return True
        return False
    def addSens(self, a, b):
        if(a == None or b == None): return False
        if(len(a) == 0 or len(b) == 0): return False
        mot = self.getLethe(a)
        if(mot == None): return False
        for e in b:
            mot.addFr(e)
        return True
    def delSens(self, a, b):
        if(a == None or b == None): return False
        if(len(a) <= 3 or len(b) == 0): return False
        mot = self.getLethe(a)
        res = False
        for e in b:
            a = mot.delFr(e)
            if(a == True): res = True
        return res
        
             
    def sprint(self, *useless):
        for e in self.l:
            print(e.en + "," + str(e.fr) + "," + str(e.pds))
        print("")
        return True        
    def sort(self, *useless): self.l.sort(key = lambda x: x.pds, reverse = True); return True
    def sortA(self, *useless): self.l.sort(key = lambda x: x.en); return True
    def getLethe(self, a, useless = None):
        for e in self.l:
            if e.en == a:
                return e
        return None
    def noBrothers(self, *useless): #A vérifier !
        self.sortA()
        for i, e in enumerate(self.l[:-1]):
            if e.en == self.l[i+1].en:
                self.l.remove(i+1)
        return True

class Lethe:
    def __init__(self, en, fr, pds = 100, gud = 0, bad = 0, last = False, row = 0):
        self.en = en
        self.fr = fr
        self.pds = float(pds)
        self.gud = int(gud)
        self.bad = int(bad)
        self.last = False
        self.row = 0
    def addFr(self, sens):
        self.fr.append(sens)
        self.fr = list(set(self.fr))
    def delFr(self, sens):
        try:
            self.fr.remove(sens)
            return True
        except ValueError: return False
    def addBad(self, i):
        if self.bad + i >= 20 and self.gud +i >= 2:
            self.addGud(-1)
        elif(self.bad >= 20): self.bad = 20
        else: self.bad += i
    def addGud(self, i):
        if self.gud + i >= 20 and self.bad + i >= 2:
            self.addBad(-1)
        elif(self.gud >= 20): self.gud = 20
        else: self.gud += i
    def addRow(self, b):
        if (b==True and (self.last == True) and self.row > -10): self.row -=1
        elif (b == False and (self.last == False) and self.row < 10): 
            self.row += 1
        elif (not(b and self.last) and self.row <= 4 and self.row >= -4):
            self.row = 0
        self.last = b
        print(colored("ROW: " + str(self.row) + " ", 'grey', 'on_white', attrs = ['bold']))       
    def setPds(self, i): self.pds = regulate(i,5,200); return True     
    def reset(self):
        self.pds = 100
        self.row = 0
        self.gud = 0
        self.bad = 0     
    def test(self, t): #LOL C BON
        if(AFFICHAGE): linePrint("GUD: "+ str(self.gud) + " ")
        if(AFFICHAGE): linePrint("BAD: "+ str(self.bad) + " ")
        if (levenshteinList(self.fr, t) <= 3):
            self.addGud(1)
            self.addRow(True)
            self.setPds(maxf(self.bad, self.gud, self.row)) #LOL COD DE MERD
            
            linePrint("Pds:" + str(int(self.pds)) + " ", None)
            print(colored("GUD: " + str(self.fr) + " ", 'white', "on_green", attrs=['bold']))
            return True
        else:
            self.addBad(1)
            self.addRow(False)
            self.setPds(maxf(self.bad, self.gud, self.row))#LOL COD DE MERD
            
            #print(colored(" PDS:" + str(self.pds), 'yellow', 'on_grey'))#LOL COD DE MERD
            #print(colored(" BAD:" + str(self.fr), 'white', 'on_red'))#LOL COD DE MERD
            linePrint("Pds:" + str(int(self.pds)) + " ", None)
            print(colored("BAD: " + str(self.fr) + " ", 'white', "on_red", attrs=['bold']))            
            return False
    def lock(self, *useless):
        self.pds = 0
        return True


def toLetheList(f): #OK
    with open(f, 'r') as f:
        r = csv.reader(f)
        l = list(r)
    return [Lethe(e[0], e[1].split(';'), e[2], e[3], e[4]) for e in l]

def save(l): #WHOOOO
    with open(FICHIER, mode='w', encoding='utf8') as f:
        for e in l:
            fr = ""
            for j in e.fr:
                fr += ";"+j
            fr = fr[1:]
            f.write(e.en+","+fr+","+str(e.pds)+","+str(e.gud)+","+str(e.bad)+"\n")

def randomPond(l): #PRRRRFFTTT
    r = random.randint(0,sum(l)-1);  i = 0 #INIT
    while(r > 0):
        r -= l[i]
        i+=1
    return i-1

if __name__ == '__main__':
    
    a = Apocryphe()
    a.save()
    
    print("PRINT--")
    a.sprint()
    print("SORT--")
    a.sort()
    print("SAVE--")
    a.save()
    print("INV--")
    a.inv(1,1)
    print("PRINT--")
    a.sprint()
    print("TO_LIST--")
    b = a.toPds()
    print(b)
    print("LEN_B: "+ str(len(b)))
    res = [0 for a in range(len(b))]
    for c in range(10000):
        r = randomPond(b)
        res[r] += 1
    print("LEN_RES: " + str(len(res)))
    print(res)
    print("EDIT--")
    a.edit("scabbard", ["bite"])
    a.sprint()
    print("ADD--")
    a.add("yes", ['oui','pourquoi pas','allez!','soyez pas vaches les mecs ?'])
    a.sprint()
    print(a.getLethe('wide'))
    print(a.getLethe('scabbard'))
    
    
    
    