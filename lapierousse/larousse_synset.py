import re


class LarousseSynset:
    def __init__(self):
        self.adress = None
        self.gramatical_category = None
        self.number = None
        self.meanings = []


class Meaning:
    def __init__(self):
        self.traduction = Traduction()
        self.exemple = Example()


class Traduction:
    def __init__(self):
        self.traduction = None
        self.metadatas = None


class Example:
    def __init__(self):
        self.example = None
        self.example_trad = None

class Metadata:
    def __init__(self):
        self.domain = None
        self.metalang = None
        self.category = None