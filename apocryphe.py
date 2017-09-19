from tools.misc import *
import random
import pickle


class Apocryphe:
    def __init__(self):
        with open('ressources/databases/jesus.pkl', 'rb') as f:  # Bdd importat°
            self.corpus = pickle.load(f)
            pass
        add_weights_to_dict(self.corpus)
        self.selected_words = sub_list_of_dict(self.corpus)

    def print(self):
        for duo in self.corpus:
            for key, _ in duo:
                print(key)

    def verify(self, answer, synsets):
        pass

    def update(self, synset, answer):
        pass

    def select(self):
        return random.choice(self.corpus)

    def save(self):
        pass

    def __str__(self):
        return '[NOT_IMPLEMENTED_YET]'


def sub_list_of_dict(dict_, broad=100):  # For
    tampax = [[key, dict_[key]] for key in dict_]
    random.shuffle(tampax)

    if broad >= len(tampax):
        broad = len(tampax) - 1

    return tampax[0:broad]


def add_weights_to_dict(dict_):
    for key in dict_:
        dict_[key] = [dict_[key], 0, 0]


def random_pond(l):
    # Init
    chosen_number = random.randint(0, sum(l)-1)
    i = 0
    # Continuation
    while chosen_number > 0:
        chosen_number -= l[i]
        i += 1
    # End
    return i-1


a = Apocryphe()
a = a.corpus['tattered']
