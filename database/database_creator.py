"""This modile provide a way to get a bdd from a list of words, with the traduction and many other cool things. But
don't say this !

"""
from nltk.corpus import wordnet as wn
from larousseparser import LarousseParser
import pickle
import time


def construct_list_of_words_to_translate(file='words_to_translate'):
    print("COMPUTING PHASE...")

    words_to_translate = set()
    for synset in wn.all_synsets():
        name = synset.name()
        if '_' not in name:
            words_to_translate.add(name[:-5])

    print("WRITING PHASE...")
    with open('../ressources/databases/' + file, 'w') as f:
        for word in words_to_translate:
            f.write(word)

    print("DONE !")
    return


def construct_synset_dictionary():
    synsets_dict = dict()
    with open('../ressources/databases/words_to_translate.txt', 'r') as f:
        for line_number, word in enumerate(f):
            word = word[:-1]
            print(line_number, 999, sep='/')
            if line_number >= 1000:
                break
            synsets_dict[word] = LarousseParser(word).feed()

    with open('../ressources/pickles/database_test.pkl', 'wb') as f:
        pickle.dump(synsets_dict, f)

    return synsets_dict


# construct_list_of_words_to_translate()
start_time = time.time()
res = construct_synset_dictionary()

for k in res:
    if res[k] is not None:
        print(k)

print("IN: %s seconds ---" % (time.time() - start_time))
