"""This module provide a good way to add words to fthe file 'words to translate' in ressources/databases.

This module will find for brothers ant will delete words to this list if they are already translated.
It's cool. OK ?

PS: EMPTY LINES = CACA
"""
import unidecode  # For accents


def remove_accents(potentially_accented_string_but_not_necessarily):
    return unidecode.unidecode(potentially_accented_string_but_not_necessarily)  # INCREDOYABLE


def normalize(word):
    if word[0] == '#':
        return ''  # To avoid comments
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


# TODO : DEPRECATED METHODE A ENLEVER ELLE EST CACA ELLE SERT A RIEN ELLE EST NULLE. BREF C'EST UNE MERDE
def simple_merge(source, target):
    words_file_1 = set()
    words_file_2 = set()

    clean_file(source)

    with open('../ressources/databases/' + source, 'r') as s:
        for line in s:
            words_file_1.add(line)

    try:
        with open('../ressources/databases/' + target, 'r') as t:
            for line in t:
                words_file_2.add(line)
    except IOError:
        print('File:', target, 'in ressources/databases was not found.')
        print('File created')

    res = words_file_1.union(words_file_2)

    with open('../ressources/databases/c.txt', 'w') as f:    # TODO: temporaire (fichier source plus tard
        for word in res:
            f.write(word)


def merge_files(target, sources):  # Sources is iterator
    words_sources = set()
    words_target = set()

    for source in sources:
        clean_file(source)
        with open('../ressources/databases/' + source, 'r') as s:
            for word in s:
                words_sources.add(word)

    try:
        with open('../ressources/databases/' + target, 'r') as t:  # Target not cleaned because of recursivity and
            # all this you see i think. If not how we say in French: 'Le fromage est dans la galette suisse,
            # mangée apr une souris hémoroidale', and we add: 'Gourgandine'.
            for word in t:
                words_target.add(word)
    except IOError:
        print('File:', target, 'in ressources/databases was not found.')
        print('File created')

    all_words = words_target.union(words_sources)

    with open('../ressources/databases/' + target, 'w') as t:
        for word in all_words:
            t.write(word)


def update_words_to_translate():
    # TODO: ca !
    pass


def similarities(source1, source2):  # O(n*ln(n)) TODO: comparer la vitesse avec &
    words_s1 = list()
    words_s2 = list()
    with open('../ressources/databases/' + source1, 'r') as s1:
        for word in s1:
            words_s1.append(word)
    with open('../ressources/databases/' + source2, 'r') as s2:
        for word in s2:
            words_s2.append(word)

    words_s1.sort()  # O(n*ln(n))
    words_s2.sort()  # O(n*ln(n))

    # Init
    pointer1 = 0
    pointer2 = 0
    container = []
    while pointer1 < len(words_s1) and pointer2 < len(words_s2):  # End O(n)
        # Cont
        #print(pointer1, pointer2)
        if words_s1[pointer1] == words_s2[pointer2]:
            container.append(words_s1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif words_s1[pointer1] < words_s2[pointer2]:
            pointer1 += 1
        else:  # words_s2[p1] > words_s2[pointer2]
            pointer2 += 1

    return container


def differences(source1, source2):  # TODO: réunir les 2 fcts ?
    words_s1 = list()
    words_s2 = list()
    with open('../ressources/databases/' + source1, 'r') as s1:
        for word in s1:
            words_s1.append(word)
    with open('../ressources/databases/' + source2, 'r') as s2:
        for word in s2:
            words_s2.append(word)

    words_s1.sort()  # O(n*ln(n))
    words_s2.sort()  # O(n*ln(n))

    # Init
    pointer1 = 0
    pointer2 = 0
    container = []
    while pointer1 < len(words_s1) and pointer2 < len(words_s2):  # End O(n)
        # Cont
        # print(pointer1, pointer2)
        if words_s1[pointer1] == words_s2[pointer2]:
            pointer1 += 1
            pointer2 += 1
        elif words_s1[pointer1] < words_s2[pointer2]:
            container.append(words_s1[pointer1])
            pointer1 += 1
        else:  # words_s2[p1] > words_s2[pointer2]
            container.append(words_s2[pointer2])
            pointer2 += 1

    return container


if __name__ == '__main__':
    print('CALCULATING...')

    # clean_file('wiki-100k.txt')
    # merge_files('caca.txt', ('a.txt', 'b.txt'))
    # a = len(similarities('wiki-100k.txt', 'words_to_translate.txt'))
    b = len(differences('wiki-100k.txt', 'words_to_translate.txt'))
    print(b)

    print("ENDED !")
