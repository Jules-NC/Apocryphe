"""LarousseSynset provide a good way to interprete Larousse.fr en-fr traductions and to convert them to a real good
database

It's jsut a way to formalise data in larousse.fr pages
"""
from collections import namedtuple


class LarousseSynset:
    def __init__(self):
        self.name = None
        self.gramatical_category = None
        self.meanings = []

    def last_meaning(self):
        if len(self.meanings) is not 0:
            return self.meanings[-1]
        return None

    def add_number(self, new_number):
        new_meaning = Meaning()
        new_meaning.number = new_number
        self.meanings.append(new_meaning)

    def set_traduction(self, new_traduction, new_metadatas):  # new_metadata is a tuple, with 3 arguments
        try:
            self.last_meaning().traduction = Traduction(new_traduction, Metadatas(*new_metadatas))
        except AttributeError:  # If last meaning doesn't exist
            raise AttributeError  # TODO: delete this error test line
            # return    TODO: remove commentary after removed precedent line

    def add_example(self, new_example, new_metadatas):  # new_metadatas is a tuple, with 3 arguments
        try:
            self.last_meaning().examples.append(Example(new_example, Metadatas(*new_metadatas)))
        except AttributeError:  # If last meaning doesn't exist
            raise AttributeError  # TODO: delete this error test line
            # return    TODO: remove commentary after removed precedent line

    def traduction(self):
        return [meaning.traduction.raw for meaning in self.meanings if meaning.traduction is not None]


class Meaning:  # Will be modified => not a tuple
    def __init__(self):
        self.number = None
        self.traduction = None
        self.examples = []


class Example:  # Will be modified => not a tuple
    def __init__(self, new_example, new_metadatas):
        self.example = new_example.raw
        self.example_trad = new_example.trad
        self.metadatas = new_metadatas


Traduction = namedtuple('Traduction', ['raw', 'metadatas'])    # Will not be changed => tuple


Metadatas = namedtuple('Metadatas', ['domain', 'metalang', 'category'])   # Will not be changed => tuple
