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


def construct_synset_dictionary(lower_bound, broad=999):
    upper_bound = lower_bound + broad
    synsets_dict = dict()
    with open('../ressources/databases/words_to_translate.txt', 'r') as f:
        for line_number, word in enumerate(f):
            if line_number < lower_bound:
                continue
            word = word[:-1]
            ETA = str((broad - (line_number - lower_bound))*3/60) + ' minutes'
            print(line_number - lower_bound, '/', broad -1, ' |ETA: ', ETA, sep='')
            if line_number >= lower_bound + broad - 1:
                break
            synsets_dict[word] = LarousseParser(word).feed()
    filename = '../ressources/pickles/database_' + str(lower_bound) + '-' + str(lower_bound + broad - 1) +'.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(synsets_dict, f)
    return synsets_dict


# construct_list_of_words_to_translate()
start_time = time.time()
res = construct_synset_dictionary(0, 10)

print('\n')
print('|==================================================|\n')
print("EXECUTION DONE !")
print("File saved !")
print("TOTAL TIME: %s seconds" % (time.time() - start_time))
