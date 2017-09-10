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

    def last_synset(self):
        try:
            return self.synsets[-1]
        except IndexError:
            print("PAS DE DERNIER SYNSET")
            raise IndexError  # TODO: à enlever après les tests

    def __str__(self):
        res = ''
        for synset in self.synsets:
            res += str(synset) + '\n|========================================|\n'
        return res


class LSynset:
    def __init__(self, new_name):
        self.name = new_name
        self.gramatical_category = None
        self.meanings = []

    def last_meaning(self):  # TODO: trouver utilité de ce truc
        if len(self.meanings) is not 0:
            return self.meanings[-1]
        return None

    def add_number(self, new_number):
        new_meaning = Meaning(new_number)
        self.meanings.append(new_meaning)

    def add_traduction(self, new_traduction, new_metadatas):  # new_metadata is a tuple, with 3 arguments
        try:
            self.last_meaning().traduction.append(Traduction(*new_traduction, Metadatas(*new_metadatas)))
        except AttributeError:  # If last meaning doesn't exist
            pass
            #raise AttributeError  # TODO: delete this error test line
            # return    TODO: remove commentary after removed precedent line

    def add_example(self, new_example, new_metadatas):  # new_metadatas is a tuple, with 3 arguments
        try:
            self.last_meaning().examples.append(Example(new_example, Metadatas(*new_metadatas)))
            print("Ajout example")
        except AttributeError:  # If last meaning doesn't exist
            raise AttributeError  # TODO: delete this error test line
            # return    TODO: remove commentary after removed precedent line

    def __str__(self):
        means = ''
        for meaning in self.meanings:
            means += str(meaning)
        return str(self.name) + '\n' + self.gramatical_category + '\n' + str(means)


class Meaning:  # Will be modified => not a tuple
    def __init__(self, new_number):
        self.number = new_number[:-1]
        self.traductions = []
        self.examples = []

    def __str__(self):
        num = '  =>(' + self.number + ')'
        trad = '    |'
        for traduction in self.traductions:
            trad += str(traduction) + '\n' # traduction can be None
        ex = '    |'
        for example in self.examples:
            ex +=  str(example) + '\n'
        return num + ':\n' + trad + ex + '\n'


Example = namedtuple('Example', ['raw', 'trad', 'metadatas'])


Traduction = namedtuple('Traduction', ['raw', 'metadatas'])    # Will not be changed => tuple


Metadatas = namedtuple('Metadatas', ['domain', 'metalang', 'category'])   # Will not be changed => tuple

if __name__ == '__main__':
    met1 = Metadatas("J'AIME LES PATES AU FROMAGE", None, None)
    ex = Example('english phrase you see ojk ?', 'Phrase anglaise capich ?', met1)

    met2 = Metadatas(None, None, 'Lol')
    trad = Traduction('bitch dick', met2)
    a = Meaning('0.')
    a.traductions.append(trad)
    a.examples.append(ex)

    print(a)
