print("\n\n\tBIENVENUE DANS LE GENERATEUR DE NOMBRES PREMIERS\n\tQUE VOULEZ-VOUS FAIRE ?")


rep = input("\n\t1 -\técraser les données et recommencer\n\t2 -\treprendre le calcul\n\t3 -\tnombres de nombres premiers actuellement calculés\n\n\tReponse : - ")

sauvegarde = 100

nom_fichier = "nombres.txt"


# recommencer le calcul
if rep == "1":
    
    # menu
    print("\n\tCe programme va écrire dans le fichier nombre des nombres premiers")
    input("\tPret à lancer ? (Appuyez sur ENTREE)   ")

    # vide le fichier
    with open(nom_fichier,"w") as fic:
        
        fic.write("2\n")
    
    nombre = 1
    liste = []
    touts_les_mots_sauvegarde = sauvegarde
    
    # boucle
    compteur = 1
    while True:
        # calcul
        while nombre <= compteur*touts_les_mots_sauvegarde :
            for i in range(2,nombre):
                if nombre%i == 0 :
                    break
                elif nombre == i+1:
                    liste.append(nombre)
            nombre +=1
        # enregistre
        with open(nom_fichier, "a") as fic :
            for i in liste :
                chaine = str(i) + "\n"
                fic.write(chaine)
        # remet les pendules à l'heure
        liste = []
        compteur += 1

# reprendre le calcul
elif rep=="2":
    
    # récupère le dernier nombre
    with open(nom_fichier,"r") as fic:
        content = fic.readlines()
        nombre = int(content[len(content)-1][0:-1])
    # écrase la dernière ligne
    with open(nom_fichier, "w") as fic:
        content.pop(len(content)-1)
        for i in content :
            fic.write(i)

    # remet les pendules à l'heure
    liste = []
    touts_les_mots_sauvegarde = sauvegarde
    
    
    reponse = input("\n\tentrez '1' pour enregistrer à chaque fois : - ")
    if reponse == "1" :
        print("\n\tSauvegarde tout les mots")
        touts_les_mots_sauvegarde = 1
    else :
        print("\n\tSauvegarde tout les 100 mots")
        touts_les_mots_sauvegarde = sauvegarde
    
    # remet le compteur au clair
    compteur = int(nombre/touts_les_mots_sauvegarde)

    # menu
    print("\n\tCe programme va écrire dans le fichier des nombres premiers depuis", nombre)
    input("\tPret à lancer ? (Appuyez sur ENTREE)   ")

    # boucle
    while True:
        # calcule tout les tants ...
        while nombre <= compteur*touts_les_mots_sauvegarde :
            for i in range(2,nombre):
                if nombre%i == 0 :
                    break
                elif nombre == i+1:
                    liste.append(nombre)
            nombre +=1

        # enregistr le tout
        with open(nom_fichier, "a") as fic :
            for i in liste :
                chaine = str(i) + "\n"
                fic.write(chaine)
        
        # prépare a un autre chargement
        liste = []
        compteur += 1

if rep == "3":
    
    with open(nom_fichier,"r") as fic :
        content = fic.readlines()
    nombre_de_nombres_premiers = len(content)
    
    print("\n\n\tIl y a actuellement",nombre_de_nombres_premiers,"nombres premiers calculés")
    input("\t")