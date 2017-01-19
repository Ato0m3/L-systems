
#!/usr/bin/env python3
import sys
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
        "taille": 10,
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


def transpo (action,angle,taille) : #création du programme pour afficher le l-system
    result = """
from turtle import *
color('black')
etats = []
"""
    #etats --> [(pos, angle), (pos1, angle1), ....]       ((x, y), angle)
    for charac in action :
            if charac == "a" :
                result += "pd();fd({});\n".format(taille)
            elif charac == "b" :
                result += "pu();fd({});\n".format(taille)
            elif charac == "+" :
                result += "right({});\n".format(angle)
            elif charac == "-" :
                result += "left({});\n".format(angle)
            elif charac == "*" :
                result += "right(180)\n"
            elif charac == "[" :
                result += "etats.append((xcor(),ycor(), heading()))\n"
            elif charac == "]":
                result += "x,y,angle = etats.pop()\n"
                result += "pu();goto(x,y);setheading(angle);pd()\n"
    result += "exitonclick()"
    return result.strip()


def verif (stockage_info,axio,reg,angle,tail,niveau) :
    if axio == None :
        print ("Erreur au niveau de l'axiome : il est obligatoire d'avoir un axiome")
        return exit()
    else :
        if len(axio) > 1 :
            print ("Erreur au niveau de l'axiome : il est obligatoire d'avoir uniquement un seul axiome")
            return exit()

        elif angle == None :
            print ("Erreur au niveau de l'angle : il est obligatoire d'avoir un angle")
            return exit()

        elif niveau == None :
            print ("Erreur au niveau du niveau :il est obligatoire d'avoir un niveau")
            return exit
        else :
            return None











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

        verif(infos,axio,reg,ang,tail,niv)

        #def création de l'axiome
        axiorendu = crea(axio,reg)
        axiofinal = creaniv(axiorendu,niv,reg)
        #print (axiofinal)

        #Création et sortie du prog final
        prog = transpo (axiofinal,ang,tail)
        print (prog)


    #mon_fichier = open("test.py", "w") # Argh j'ai tout écrasé !
    #mon_fichier.write(prog)
    #mon_fichier.close()
