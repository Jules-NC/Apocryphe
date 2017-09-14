"""This modile provide a way to get a bdd from a list of words, with the traduction and many other cool things. But
don't say this !

"""
from larousseparser import LarousseParser
from nltk.corpus import wordnet as wn
import concurrent.futures
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


def construct_synset_dictionary(lower_bound, broad=1000):
    if lower_bound + broad > 55754:
        broad = 55754 - lower_bound
    synsets_dict = dict()
    with open('../ressources/databases/words_to_translate.txt', 'r') as f:
        for line_number, word in enumerate(f):
            if line_number < lower_bound:
                continue
            word = word[:-1]
            print(word)
            eta = str((broad - (line_number - lower_bound))*0.7/60) + ' minutes'
            print('BEGIN: ', lower_bound, '| ', line_number - lower_bound, '/', broad - 1, ' |ETA: ', eta, sep='')
            if line_number >= lower_bound + broad - 1:
                break
            synsets_dict[word] = LarousseParser(word).feed()
    filename = '../ressources/pickles/database_' + str(lower_bound) + '-' + str(lower_bound + broad -1) + '.pkl'
    with open(filename, 'wb') as f:
        pickle.dump(synsets_dict, f)
    return synsets_dict


# construct_list_of_words_to_translate()
start_time = time.time()
#debuts = [a for a in range(49000, 51000, 1000)]
construct_synset_dictionary(55000)

#with concurrent.futures.ThreadPoolExecutor(4) as executor:
#    executor.map(construct_synset_dictionary, debuts)

print('\n')
print('|==================================================|\n')
print("EXECUTION DONE !")
print("File saved !")
print("TOTAL TIME: %s seconds" % (time.time() - start_time))
