# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup   # To get a beautifil string to the end. I don't use this module for something else.
import urllib.request   # To get content from internet and use him with beautifulsoup4
import larousse_synset  # For Objects in this


class LarousseParser:
    def __init__(self, text):
        self.beautiful_data = [line.strip() for line in text.split('\n')]
        self.in_td = False

        # Informations utiles
        self.adresse = None
        self.categorie_grammaticale = None
        self.numero = None
        self.indicateur_domaine = None  # EXAMPLE
        self.metalangue = None  # (example)
        self.indicateur = None  # [example]
        self.traduction = None
        self.exemple = None
        self.trad_exemple = None

        for l in self.beautiful_data:
            print(l)
        print(len(self.beautiful_data))


if __name__ == '__main__':
    data = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/plant').read().decode('utf8')
    data = str(BeautifulSoup(data, 'html.parser').prettify())
    parser = LarousseParser(data)
