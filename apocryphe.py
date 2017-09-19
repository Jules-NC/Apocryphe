import random
import pickle


class Apocryphe:
    def __init__(self):
        with open('ressources/databases/jesus.pkl', 'rb') as f:  # Bdd importat°
            self.corpus = pickle.load(f)
            pass

        self.corpus = list(self.corpus)



def dict_to_list_with_tuples():
    pass



a = Apocryphe()
a = a.corpus['tattered']
# print(a)
for trad in a.all_translations():
    print(trad)
    pass