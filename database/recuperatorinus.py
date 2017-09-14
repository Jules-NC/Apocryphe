import pickle
noms_fichiers = ['database_' + str(x) + '-' + str(x+1000-1) + '.pkl' for x in range(0, 55001, 1000)]


quantic_soup = list()

for nom_fichier in noms_fichiers:  # TODO: LIST COMPREHENSION
    with open('../ressources/pickles/' + nom_fichier, 'rb') as f:
        quantic_soup.append(pickle.load(f))

jesus = quantic_soup[0]
for osti in range(1, len(quantic_soup)):
    jesus.update(quantic_soup[osti])

c = 0
for osti in jesus:
    if osti == 'heretic':    # TODO: Vérifier la condition > 1700 lignes. Si c'est pas ca je ss gouaké
        c += 1
        print(jesus[osti])
print("TOT:", c)
