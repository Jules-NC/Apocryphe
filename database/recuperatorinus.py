import pickle
files_names = ['database_' + str(x) + '-' + str(x + 1000 - 1) + '.pkl' for x in range(0, 55001, 1000)]


def recuperate():
    quantic_soup = list()

    for nom_fichier in files_names:  # TODO: LIST COMPREHENSION
        with open('../ressources/pickles/' + nom_fichier, 'rb') as f:
            quantic_soup.append(pickle.load(f))

    jesus = quantic_soup[0]
    for hosti in range(1, len(quantic_soup)):
        jesus.update(quantic_soup[hosti])

    jesus_2_le_retour = {key:value for key, value in jesus.items() if value is not None}  # Car peut aps changer taille
    #  cours d'éxécution...

    with open('../ressources/databases/jesus.pkl', 'wb') as f:
        pickle.dump(jesus_2_le_retour, f)

    print("FICHIER ENREGISTRE")


if __name__ == '__main__':
    recuperate()
