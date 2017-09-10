# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup   # To get a beautifil string to the end. I don't use this module for something else.
import urllib.request   # To get content from internet and use him with beautifulsoup4
from larousse_synset import *


class LarousseParser:
    def __init__(self, text):
        self.in_td = False
        self.lines = [line.strip() for line in text.split('\n')]
        self.l_synsets = LSynsets()

        self.example_raw = None

        self.domain_indicator = None  # EXAMPLE
        self.metalang = None  # (example)
        self.category_indicator = None  # [example]

    def add_urgent_meaning(self):
        self.l_synsets.last_synset().add_number('1.')

    def reset_metadatas(self):
        self.domain_indicator = None
        self.metalang = None
        self.category_indicator = None

    def feed(self):
        for line_number, line in enumerate(self.lines):
            if '<td' in line:  # For categoty
                self.in_td = True
            elif '/td' in line:  # Idem
                self.in_td = False

            # Adresse => new LarousseSynset(name)
            if 'Adresse' in line:
                name = data(self.lines, line_number)
                self.l_synsets.add_synset(LSynset(name))

            # number => new Meaning(number)
            elif 'numero' in line:
                number = data(self.lines, line_number, 2)
                self.l_synsets.last_synset().add_number(number)

            elif 'CategorieGrammaticale' in line and self.in_td is not True:
                gram_category = data(self.lines, line_number, 1)  # TODO: 1., 2., 5. rectification to int
                self.l_synsets.last_synset().gramatical_category = gram_category

            elif 'IndicateurDomaine' in line:  # TODO: vérifier si ces 2 conditions doivent être dans cet ordre
                self.domain_indicator = data(self.lines, line_number)
            elif 'Indicateur' in line:
                self.category_indicator = data(self.lines, line_number)
            elif 'Metalangue' in line:
                self.metalang = data(self.lines, line_number)

            elif 'lienarticle2' in line:
                if len(self.l_synsets.last_synset().meanings) is 0:
                    self.add_urgent_meaning()
                traduction = data(self.lines, line_number)
                metadatas = (self.domain_indicator, self.metalang, self.category_indicator)  # TODO: a method for this
                self.l_synsets.last_synset().add_traduction(traduction, metadatas)
                self.reset_metadatas()

            elif 'Locution2' in line:
                self.example_raw = data(self.lines, line_number)
            elif 'Traduction2' in line:
                if len(self.l_synsets.last_synset().meanings) is 0:
                    self.add_urgent_meaning()
                example_trad = data(self.lines, line_number)
                traduct = (self.example_raw, example_trad)
                metadatas = (self.domain_indicator, self.metalang, self.category_indicator)
                self.l_synsets.last_synset().add_example(traduct, metadatas)
                self.example_raw = None
                self.reset_metadatas()

        return self.l_synsets


def data(your_list, line_number, offset=1):
    return your_list[line_number + offset]


if __name__ == '__main__':
    raw_data = urllib.request.urlopen('http://www.larousse.fr/dictionnaires/anglais-francais/as')
    raw_data = raw_data.read().decode('utf8')
    raw_data = str(BeautifulSoup(raw_data, 'html.parser').prettify())

    print("ACCES AUX SITE..")
    parser = LarousseParser(raw_data)
    print(parser.feed())
