"""This modile provide a way to get a bdd from a list of words, with the traduction and many other cool things. But
don't say this !

"""
from larousseparser import LarousseParser
from nltk.corpus import wordnet as wn
from threading import Thread
import pickle
import time


def construct_list_of_words_to_translate(file='words_to_translate.txt'):
    print("COMPUTING PHASE...")

    words_to_translate = set()
    for synset in wn.all_synsets():
        name = synset.name()
        if '_' not in name and '-' not in name and '.' not in name[:-5]:
            words_to_translate.add(name[:-5])

    print("WRITING PHASE...")
    with open('../ressources/databases/' + file, 'w') as f:
        for word in words_to_translate:
            f.write(word + '\n')

    print("DONE !")
    return

class ConstructDict(Thread):
    def __init__(self, lower_b, broad_=1000):
        Thread.__init__(self)
        self.lower_bound = lower_b
        self.broad = broad_
        self.construct_synset_dictionary()

    def construct_synset_dictionary(self):
        if self.lower_bound + self.broad > 55574:
            broad = 55574 - self.lower_bound
        synsets_dict = dict()
        with open('../ressources/databases/words_to_translate.txt', 'r') as f:
            for line_number, word in enumerate(f):
                if line_number < self.lower_bound:
                    continue
                word = word[:-1]
                eta = str((self.broad - (line_number - self.lower_bound))*0.7/60) + ' minutes'
                print('BEGIN: ', self.lower_bound, '| ', line_number - self.lower_bound, '/', self.broad - 1, ' |ETA: ',
                      eta,
                      sep='')
                if line_number >= self.lower_bound + self.broad - 1:
                    break
                synsets_dict[word] = LarousseParser(word).feed()
        filename = '../ressources/pickles/database_' + str(self.lower_bound) + '-' + str(self.lower_bound + self.broad -
                                                                                         1) + '.pkl'
        with open(filename, 'wb') as f:
            pickle.dump(synsets_dict, f)
        return synsets_dict


# construct_list_of_words_to_translate()
start_time = time.time()

res = [ConstructDict(lower_bound).start() for lower_bound in range(0, 10000, 1000)]

print('\n')
print('|==================================================|\n')
print("EXECUTION DONE !")
print("File saved !")
print("TOTAL TIME: %s seconds" % (time.time() - start_time))
