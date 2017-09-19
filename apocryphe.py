import random
import pickle


class Apocryphe:
    def __init__(self):
        with open('ressources/databases/jesus.pkl', 'rb') as f:  # Bdd importat°
            self.corpus = pickle.load(f)
            pass

        self.corpus = dict_to_list_with_tuples(self.corpus)
        random.shuffle(self.corpus)
        self.corpus = self.corpus[0:100]

    def print(self):
        for duo in self.corpus:
            for key, _ in duo:
                print(key)

    def select(self):
        return random.choice(self.corpus)


def dict_to_list_with_tuples(dict_):
    return [(key, dict_[key]) for key in dict_]


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
# print(a)
for trad in a.all_translations():
    print(trad)
    pass