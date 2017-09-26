"""LarousseSynset provide a good way to interpret Larousse.fr en-fr traductions and to convert them to a real good
database.

It's just a way to formalise data in larousse.fr pages
"""

from collections import namedtuple
from termcolor import colored


class LSynsets:
    def __init__(self):
        self.synsets = []

    def add_synset(self, synset):
        self.synsets.append(synset)

    def last_synset(self):
        try:
            return self.synsets[-1]
        except IndexError:
            return LSynset('DUMMY')  # TODO: Comprendre le comportement de cet objet

    def delete_useless_synset(self):
        for i, synset in enumerate(self.synsets):
            if len(synset.meanings) is 0:
                del self.synsets[i]
            try:
                self.synsets[i].delete_useless_meanings()
            except IndexError:
                pass

    def names(self):
        return [name.name for name in self.synsets]

    def all_translations(self):
        return [translation.raw for lsynset in self.synsets for translation in lsynset.all_translations()]

    def __str__(self):
        res = ''
        for synset in self.synsets:
            res += str(synset) + '\n'
        return res


class LSynset:
    def __init__(self, new_name):
        self.name = new_name
        self.gramatical_category = None
        self.meanings = []

    def last_meaning(self):  # TODO: peut être excéption: vérifier
        if len(self.meanings) is not 0:
            return self.meanings[-1]

    def add_number(self, new_number):
        new_meaning = Meaning(new_number)
        self.meanings.append(new_meaning)

    def add_traduction(self, new_traduction, new_metadatas):  # new_metadata is a tuple, with 3 arguments
        self.last_meaning().traductions.append(Traduction(new_traduction, Metadatas(*new_metadatas)))

    def add_example(self, new_example, new_metadatas):  # new_metadatas is a tuple, with 3 arguments
        self.last_meaning().examples.append(Example(new_example[0], new_example[1],  Metadatas(*new_metadatas)))

    def delete_useless_meanings(self):
        for i, meaning in enumerate(self.meanings):
            if len(meaning.traductions) is 0 and len(meaning.examples) is 0:
                del self.meanings[i]

    def all_translations(self):
        return [translation for meaning in self.meanings for translation in meaning.all_translations()]

    def __str__(self):
        means = ''
        for meaning in self.meanings:
            means += str(meaning)
        name = colored(str(self.name.upper()), 'yellow', attrs=['bold'])
        gramatical_category = colored(str(self.gramatical_category), 'cyan')
        return name + '\n' + gramatical_category + '\n' + str(means)


class Meaning:  # Will be modified => not a tuple
    def __init__(self, new_number):
        self.number = new_number[:-1]
        self.traductions = []
        self.examples = []

    def all_translations(self):
        return [a for a in self.traductions]

    def __str__(self):  # Weird code but beautiful print ^^
        num = '  =>(' + self.number + ')'
        traduct = ''
        for traduction in self.traductions:
            metadatas = str_metadatas(traduction.metadatas)
            after = ''
            if len(metadatas) is not 0:
                after = colored('| ', 'cyan')
            translat = colored(str(traduction.raw).strip(), 'grey', 'on_white')
            traduct += colored('    |', 'cyan', attrs=['bold']) + metadatas + after + translat + '\n'

        examp = ''
        for example in self.examples:
            metadatas = str_metadatas(example.metadatas)
            ex = str_example(example)
            after = ''
            if len(metadatas) is not 0:
                after = colored('} ', 'magenta')
            if example.raw is not None:  # TODO: BUG UNCERTAINTY dans parser !!! WTF LAROUSSE !
                examp += '    ' + colored('{', 'magenta', attrs=['bold']) + metadatas + after + ex + '\n'
        return num + ':\n' + traduct + examp + '\n'


Example = namedtuple('Example', ['raw', 'trad', 'metadatas'])


Traduction = namedtuple('Traduction', ['raw', 'metadatas'])    # Will not be changed => tuple


Metadatas = namedtuple('Metadatas', ['domain', 'metalang', 'category'])   # Will not be changed => tuple


def str_metadatas(met):
    res = ''
    if met.domain is not None:
        res += colored(met.domain, 'red')
    if met.metalang is not None:
        if len(res) is not 0:
            res += ', '
        res += colored(met.metalang[1:-1], 'green')
    if met.category is not None:
        if len(res) is not 0:
            res += ', '
        if met.category[0:3] == ' - ':
            category = met.category[3:]
            res += category
        else:
            res += colored(met.category[1:-1], 'blue')
    return res


def str_example(ex):
    res = ''
    res += colored(ex.raw, 'magenta')
    res += ' ==> '
    res += colored(ex.trad, 'magenta')
    return res

if __name__ == '__main__':  # TEST ONLY ! IT'S A MODULE !

    b = LSynset('NOM')  # Création LSynset
    b.gramatical_category = 'nounent'  # On met ce paramètre
    b.add_number('0')  # Création et ajout d'un Meaning dans le synset

    met1 = ("J'AIME LES PATES AU FROMAGE", None, None)
    met2 = (None, None, 'Lol')

    trad = Traduction('bitch dick', met1)
    ex = ('english phrase you see ojk ?', 'Phrase anglaise capich ?', met1)

    b.add_traduction(trad, met1)
    b.add_example(ex, met2)

    print(b)
