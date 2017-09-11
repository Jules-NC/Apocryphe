"""This modile provide a way to get a bdd from a list of words, with the traduction and many other cool things. But
don't say this !

"""
from nltk.corpus import wordnet as wn


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
            f.write(word + '\n')

    print("DONE !")
    return

def construct_synset_dictionnary(file='synset_dictionnary'):
    pass