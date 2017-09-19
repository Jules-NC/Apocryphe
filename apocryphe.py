import random
import pickle


class Apocryphe:
    def __init__(self):
        with open('ressources/databases/jesus.pkl', 'rb') as f:  # Bdd importat°
            self.corpus = pickle.load(f)
            pass
        add_weight_to_dict(self.corpus)
        self.selected_words = sub_dict(self.corpus)

    def print(self):
        for duo in self.corpus:
            for key, _ in duo:
                print(key)

    def select(self):
        return random.choice(self.corpus)


def sub_dict(dict_, broad=100):
    tampax = [[key, dict_[key]] for key in dict_]
    random.shuffle(tampax)

    if broad >= len(tampax):
        broad = len(tampax) - 1

    return tampax[0:broad]


def add_weight_to_dict(dict_):
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
