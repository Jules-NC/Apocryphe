from tools.misc import *
import random
import pickle


class Apocryphe:  # TOUTE RECHERCHE ICI EST LINEAIRE. SI VOUS N ETES PAS CONTENTS DOMMAGE !
    def __init__(self):
        with open('ressources/databases/jesus.pkl', 'rb') as f:  # Bdd importat°
            corpus = pickle.load(f)
            pass

        self.dictionary = init_sub_corpus(corpus, 100)  # dict
        self.locks = []  # list of keys
        self.weights = init_weights(self.dictionary)  # dict of weights for optimisation
        self.historique = init_history(self.dictionary)
        # TODO: fera un filtre de convolution d'apprentissage avec ca && transmettre ca à un serveur.

    def print(self):
        for duo in self.corpus:
            for key, _ in duo:
                print(key)

    def verify(self, answer, synsets):
        pass

    def update_weights(self):  # TODO: ca !
        for key in self.dictionary:
            # self.weights[key] = GAUSS_LIKE FUNC OR ANYTHING
            pass

    def __str__(self):
        return '[NOT_IMPLEMENTED_YET]'


def init_sub_corpus(dict_, broad=100):  # DEGEULASSE !!!
    temporary_list = [[key, dict_[key]] for key in dict_]
    random.shuffle(temporary_list)

    if broad >= len(temporary_list):
        broad = len(temporary_list) - 1

    temporary_list = temporary_list[0:broad]
    return {item[0]:item[1] for item in temporary_list}


def init_history(dict_):
    return {key:[] for key in dict_}


def init_weights(dict_):
    return {key:0 for key in dict_}


def random_pond(l):  # TODO: poss: faire ca maisa avec a et b comme ca on est bien
    # Init
    chosen_number = random.randint(0, sum(l)-1)
    i = 0
    # Continuation
    while chosen_number > 0:
        chosen_number -= l[i]
        i += 1
    # End
    return i-1

if __name__ == '__main__':
    a = Apocryphe()
