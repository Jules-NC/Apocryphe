# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 01:40:32 2017

@author: Lambyor
CC LEVENSTHEIN TO WIKIPEDIA ALGORITHM

Ah oui j'ai voulu mettre des tests mais en fait c'est chiant alors si vous voulez modifier bah bonne chance. 
"""
from ROLF import *
#from translate import Translator
import numpy as np
import math
#translator= Translator(to_lang="fr") #GLOBAL

#translator.translate("This is a pen.")

def levenshtein(source, tg): #UTSUKUSHI DESU DESU MOTTO MOTTO NOTICE ME SEMPAI
    if len(source) < len(tg): return levenshtein(tg, source)
    if len(tg) == 0: return len(source)
    source = np.array(tuple(source)); tg = np.array(tuple(tg))
    p_r = np.arange(tg.size + 1)
    for s in source:
        c_r = p_r + 1; c_r[1:] = np.minimum(c_r[1:],np.add(p_r[:-1], tg != s))
        c_r[1:] = np.minimum(c_r[1:], c_r[0:-1] + 1); p_r = c_r
    return p_r[-1]

def levenshteinList(l, tg):
    try: return min([levenshtein(e, tg) for e in l])
    except ValueError: return 100

def gauss(x, y, s, A = 1, x0 = 0, y0= 0, sX = 1, sY = 1):
    #Oui des librairies font ca très bien
    #...
    #...
    #...
    #MAIS J'AI PAS LE TEMPS
    #Mot-Dièse MADLAB !
    return A*math.exp(-((x-x0)**2/(2*sX**2)+ (y-y0)**2/(2*sY**2)))+ 8.3*s

def maxf(x,y,s):
    """
    >>> max(0,0,0)
    100
    """
    #C'est l'histoire d'un bloc dont on oubliera la signification...
    return max(gauss(x, y, s, 100, 0, 0, 3.6, 1.9), 
               gauss(x, y, s, 100, 10, 0, 4.5, 3.75), 
               gauss(x, y, s, 100, 20, 0, 6.4, 7.8))

def regulate(e, a, b):
    #Assert est très très très utile la !
    assert a < b
    if e <= a: e = a
    elif e >= b: e = b
    assert e >= a
    assert e <= b
    return e

def importF(a = False): #UN PEU DE LA MERDE, RIEN NE VAUT UN HUMAIN
    if a == False : return
    with open(IMPORTATION, mode='r', encoding='utf8') as f:
        r = csv.reader(f)
        l = list(r)
    with open(FICHIER, mode='r', encoding='utf8') as f:
        for e in l:
            if (not(a)): break
            #f.write
            print((e[0] +","+str(e[1])+",100,0,0"))


if __name__ == '__main__':
    #print('Languages:', translate.langs)
    #print('Translate directions:', translate.directions)
    #print('Detect language:', translate.detect('Привет, мир!'))
    #print('Translate:', translate.translate('rip', 'en-fr'))  # or just 'en'
    #print('Translate:', translate.translate('crust', 'en-fr')['text'][0])  # or just 'en'    
    
    print(levenshtein("", "abc"))
    print(maxf(20,0,9))
    a = ["manger","mangea","mangaient"]
    print(levenshteinList(a, "mangeaies"))
    importF(True) #True si oui #Tautologie