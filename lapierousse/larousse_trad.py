# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import re

class larousse_parser():
    def __init__(self, data):
        self.beautiful_data = [line.strip() for line in data.split('\n')]
        self.in_td = False

        # Informations utiles
        self.adresse = None
        self.categorie_grammaticale = None
        self.numero = None
        self.indicateur_domaine = None  # EXAMPLE
        self.metalangue = None  #  (example)
        self.indicateur = None  # [example]
        self.traduction = None
        self.exemple = None
        self.trad_exemple = None

        for l in self.beautiful_data:
            print(l)
        print(len(self.beautiful_data))

        def feed():
            pass

if __name__ == '__main__':
    data = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/plant').read().decode('utf8')
    data = str(BeautifulSoup(data, 'html.parser').prettify())
    parser = larousse_parser(data)
