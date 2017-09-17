import random
import pickle
import os  # TODO: retirer


class Apocryphe:
    def __init__(self):
        with open('ressources/databases/jesusz.pkl', 'w') as f:
            f.write('lol')
            # self.corpus = pickle.load(f)
            pass
        print(type(self.corpus))


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
print(get_immediate_subdirectories('.'))