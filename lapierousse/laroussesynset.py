"""LarousseSynset provide a good way to interprete Larousse.fr en-fr traductions and to convert them to a real good
database

It's jsut a way to formalise data in larousse.fr pages
"""

from collections import namedtuple


class LSynsets:
    def __init__(self):
        self.synsets = []

    def add_synset(self, synset):
        self.synsets.append(synset)

    def last_synset(self):  # TODO: vérifier excéption
        return self.synsets[-1]

    def delete_useless_synset(self):
        if len(self.synsets) is 1:
            del self.synsets[0]
        for i, synset in enumerate(self.synsets):
            if len(synset.meanings) is 0:
                del self.synsets[i]
            try:
                self.synsets[i].delete_useless_meanings()
            except IndexError:
                pass

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

    def __str__(self):
        means = ''
        for meaning in self.meanings:
            means += str(meaning)
        return str(self.name.upper()) + '\n' + str(self.gramatical_category) + '\n' + str(means)


class Meaning:  # Will be modified => not a tuple
    def __init__(self, new_number):
        self.number = new_number[:-1]
        self.traductions = []
        self.examples = []

    def __str__(self):  # Weird code but beautiful print ^^
        num = '  =>(' + self.number + ')'
        traduct = ''
        for traduction in self.traductions:
            traduct += '    |' + '(' + str(traduction.metadatas.domain) + ', ' + str(traduction.metadatas.metalang) +\
                       ' , ' + str(traduction.metadatas.category) + ') ' + str(traduction.raw) + '\n'
        examp = ''
        for example in self.examples:
            examp += '    {' + '(' + str(example.metadatas.domain) + ', ' + str(example.metadatas.metalang) +\
                       ' , ' + str(example.metadatas.category) + ') ' + str(example.raw) + ' ==> ' + str(example.trad)\
                     + '\n'
        return num + ':\n' + traduct + examp + '\n'


Example = namedtuple('Example', ['raw', 'trad', 'metadatas'])


Traduction = namedtuple('Traduction', ['raw', 'metadatas'])    # Will not be changed => tuple


Metadatas = namedtuple('Metadatas', ['domain', 'metalang', 'category'])   # Will not be changed => tuple


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
