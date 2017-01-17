#!/usr/bin/env python3

"""                        000000000000000000000
                        000_Programme L-systems_000
                           000000000000000000000

        -Ouvre un fichier contenant axiome, règles, angle, taille et niveau ;
        -Créer un L-systems à partir de ces infos ;
        -Sort un programme permettant de dessiner le L-systems;

                                            """

if __name__ == "__main__" :

    with open(input("Entrer le nom de votre fichier :")) as f : #Ouverture et lecture du fichier
        t= f.readlines()

        stockage_info= {}  #Espace de stockage des informatins (axiome, règles ect...)

        def Recup (x) :     #Fonction de récuparation des données du fichier
            for line in x :
                if line.startswith("axiome"):
                    line = line.split("=")
                    stockage_info["Axiome"]= line[1]
                elif line.startswith("angle"):
                    line = line.split("=")
                    stockage_info["Angle"]= line[1]
                elif line.startswith("taille"):
                    line = line.split("=")
                    stockage_info["Taille"]= line[1]
                elif line.startswith("niveau"):
                    line = line.split("=")
                    stockage_info["Niveau"]= line[1]




        Recup(t) #application sur le fichier donné


        #print (stockage_info["Axiome"])
        #print (stockage_info["Angle"])
        #print (stockage_info["Taille"])
        #print (stockage_info["Niveau"])
        print (stockage_info)
