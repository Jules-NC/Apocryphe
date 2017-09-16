"""This module provide a good way to add words to fthe file 'words to translate' in ressources/databases.

This module will find for brothers ant will delete words to this list if they are already translated.
It's cool. OK ?

PS: EMPTY LINES = CACA
"""
import unidecode  # For accents


def remove_accents(potentially_accented_string_but_not_necessarily):
    return unidecode.unidecode(potentially_accented_string_but_not_necessarily)  # INCREDOYABLE


def normalize(word):
    word = remove_accents(word)  # No accents
    if not word.islower():  # No caps
        word = word.lower()
    aryans_letters = 'abcdefghijklmnopqrstuvwxyz'  # Superior letters
    for letter in word:  # No other letters than [a-z]
        if letter not in aryans_letters:
            word = word.replace(letter, '')

    return word  # Ouah ! Perfect word


def clean_file(source):
    with open('../ressources/databases/' + source, 'r') as f:
        words_set = set()
        for word in f:
            word = normalize(word)
            if len(word) > 0:
                words_set.add(word + '\n')

    with open('../ressources/databases/' + source, 'w') as f:
        for word in words_set:
            f.write(word)


def simple_merge(source, target):
    words_file_1 = set()
    words_file_2 = set()

    clean_file(source)

    with open('../ressources/databases/' + source, 'r') as s:
        for line in s:
            words_file_1.add(line)

    with open('../ressources/databases/' + target, 'r') as t:
        for line in t:
            words_file_2.add(line)
    res = words_file_1.union(words_file_2)

    with open('../ressources/databases/c.txt', 'w') as f:    # TODO: temporaire (fichier source plus tard
        for word in res:
            f.write(word)


def merge(target, sources):  # Sources is iterator
    words_sources = set()
    words_target = set()

    for source in sources:
        clean_file(source)
        with open('../ressources/databases/' + source, 'r') as s:
            for word in s:
                words_sources.add(word)

    with open('../ressources/databases/' + target, 'r') as t:
        for word in t:
            words_target.add(word)

    all_words = words_target.union(words_sources)

    with open('../ressources/databases/' + target, 'w') as t:
        for word in all_words:
            t.write(word)


if __name__ == '__main__':
    #clean_file('a.txt')
    #simple_merge('a.txt', 'b.txt')
    merge('c.txt', ('a.txt', 'b.txt'))