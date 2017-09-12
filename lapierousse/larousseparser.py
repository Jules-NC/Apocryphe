# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup   # To get a beautifil string to the end. I don't use this module for something else.
import urllib.request   # To get content from internet and use him with beautifulsoup4
from laroussesynset import *
import time  # for connexions exceptions


URL = 'http://www.larousse.fr/dictionnaires/anglais-francais/'


class LarousseParser:
    def __init__(self, word):
        raw_data = None
        error = True   # Just to simulate a DO/While
        while error:
            try:
                raw_data = urllib.request.urlopen(URL + word)
                error = False
            except Exception:
                print('Retry')
                time.sleep(2)
                pass

        raw_data = raw_data.read().decode('utf8')
        raw_data = str(BeautifulSoup(raw_data, 'html.parser').prettify())

        self.in_trad = False

        self.lines = [line.strip() for line in raw_data.split('\n')][1700:]  # 1700 because the content begin after 1700
        self.l_synsets = LSynsets()

        self.in_td = False
        self.example_raw = None
        self.domain_indicator = None  # EXAMPLE
        self.metalang = None  # (example)
        self.category_indicator = None  # [example]

    def _reset_metadatas(self):
        self.domain_indicator = None
        self.metalang = None
        self.category_indicator = None

    def add_urgent_meaning(self):   # When you don't have any number but traductions (ex: 'tattered')
        self.l_synsets.last_synset().add_number('1.')

    def feed(self):
        for line_number, line in enumerate(self.lines):
            if 'article_bilingue' in line:  # Before this, we don't want 'Traduction' class
                self.in_trad = True

            if not self.in_trad:  # ==> Usefull data => we continue
                continue

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

            elif 'IndicateurDomaine' in line:
                self.domain_indicator = data(self.lines, line_number)

            elif 'Indicateur' in line:
                self.category_indicator = data(self.lines, line_number)

            elif 'Metalangue' in line:
                self.metalang = data(self.lines, line_number)

            # Cover all 'Traduction' possibilities
            elif 'Traduction' in line and 'Traduction2' not in line and self.in_trad:
                if len(self.l_synsets.last_synset().meanings) is 0:
                    self.add_urgent_meaning()
                traduction = ''
                i = line_number + 1
                while '/span' not in self.lines[i]:
                    if '<span' in self .lines[i]:   # M/F bug and useless data
                        i += 2
                        traduction += ' '
                    if '<small' in self.lines[i]:   # OR bug (word1orword2 => word1 OR word2)
                        traduction += ' ' + self.lines[i+1].upper() + ' '
                        i += 2
                    if 'lienconj2' in self.lines[i]:
                        i += 2
                    if '<' not in self.lines[i]:
                        traduction += self.lines[i]
                    i += 1
                metadatas = (self.domain_indicator, self.metalang, self.category_indicator)  # TODO: a method for this
                self.l_synsets.last_synset().add_traduction(traduction, metadatas)
                self._reset_metadatas()

            elif 'Locution2' in line:
                self.example_raw = data(self.lines, line_number)

            # Traduction2 find ==> we can save the example
            elif 'Traduction2' in line:
                if len(self.l_synsets.last_synset().meanings) is 0:
                    self.add_urgent_meaning()
                example_trad = data(self.lines, line_number)
                traduct = (self.example_raw, example_trad)
                metadatas = (self.domain_indicator, self.metalang, self.category_indicator)
                self.l_synsets.last_synset().add_example(traduct, metadatas)
                self.example_raw = None
                self._reset_metadatas()

        self.l_synsets.delete_useless_synset()
        if len(self.l_synsets.synsets) is 0:
            self.l_synsets = None
        return self.l_synsets


def data(your_list, line_number, offset=1):
    return your_list[line_number + offset]


if __name__ == '__main__':
    start_time = time.time()
    b = LarousseParser('seizing').feed()
    print(b)
    print("%s seconds ---" % (time.time() - start_time))
