import pickle
noms_fichiers = ['database_' + str(x) + '-' + str(x+1000-1) + '.pkl' for x in range(0, 55001, 1000)]


quantic_soup = list()

for nom_fichier in noms_fichiers:  # TODO: LIST COMPREHENSION
    with open('../ressources/pickles/' + nom_fichier, 'rb') as f:
        quantic_soup.append(pickle.load(f))

jesus = quantic_soup[0]
jesus = [jesus.update(osti) for osti in quantic_soup[1:]]
for osti in jesus:
    print(osti)