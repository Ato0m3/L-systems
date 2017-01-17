
#!/usr/bin/env python3

"""                        000000000000000000000
                        000_Programme L-systems_000
                           000000000000000000000
        -Ouvre un fichier contenant axiome, règles, angle, taille et niveau ;
        -Créer un L-systems à partir de ces infos ;
        -Sort un programme permettant de dessiner le L-systems;
                                            """


def recup(fichier) :     # Fonction de récuparation des données du fichier
    stockage_info = {
        "axiome": None,
        "angle": None,
        "taille": None,
        "regles": {},
        "niveau": None
    }  # Espace de stockage des informatins (axiome, règles ect...)
    regle = False
    for line in fichier:
        if line.startswith("axiome"):
            regle = False
            axiome = line.split("=")[1].replace("\"", "").strip()
            stockage_info["axiome"] = axiome
        elif line.startswith("angle"):
            regle = False
            angle = float(line.split("=")[1].strip())
            stockage_info["angle"] = angle
        elif line.startswith("taille"):
            regle = False
            taille = float(line.split("=")[1].strip())
            stockage_info["taille"] = taille
        elif line.startswith("niveau"):
            regle = False
            niveau = int(line.split("=")[1].strip())
            stockage_info["niveau"] = niveau
        elif line.startswith("regle"):
            line = line.split("=")
            regle = True
        elif regle == True:
            r = line.replace("\"", "")
            left, right = r.split("=")
            left, right = left.strip(), right.strip()
            stockage_info["regles"][left] = right
    return stockage_info


def crea (axiome,regles) : #créa de l'axiome pour un niveau

    result = ""
    for letter in axiome:
        if letter in regles:
            result += regles[letter]
        else :
            result += letter
    return result


def creaniv (x,niveau,regles) :  #applique le niveau
    result = ""
    for level in range (1 ,niveau):
        x = crea(x,regles)
    return x


def transpo (axiodef,angle,taille) : #création du programme pour afficher le l-system
    result = ""
    for string in axiodef :
        if string == "a" :
            result += "pd();fd({});\n".format(taille)
        elif string == "b" :
            result += "pu();fd({});\n".format(taille)
        elif string == "+" :
            result += "right({});\n".format(angle)
        elif string == "-" :
            result += "left({});\n".format(angle)
        elif string == "*" :
            result += "right(180)"
        elif string == "[" :
            result += " "
    return result










if __name__ == "__main__" :
    with open(input("Entrer le nom de votre fichier :")) as f : #Ouverture et lecture du fichier
        t = f.readlines()
        infos = recup(t) #application sur le fichier donné
        #print(infos)

        #def variables
        axio = infos["axiome"]
        reg = infos["regles"]
        niv = infos["niveau"]
        ang = infos["angle"]
        tail = infos["taille"]

        #def création de l'axiome
        axiorendu = crea(axio,reg)
        axiofinal = creaniv(axiorendu,niv,reg)
        #print (axiofinal)

        #Création et sortie du prog final
        prog = transpo (axiofinal,ang,tail)
        print ('from turtle import * \ncolor("black")\n',prog ,sep='')
