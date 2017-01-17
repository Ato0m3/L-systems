
#!/usr/bin/env python3

"""                        000000000000000000000
                        000_Programme L-systems_000
                           000000000000000000000
        -Ouvre un fichier contenant axiome, règles, angle, taille et niveau ;
        -Créer un L-systems à partir de ces infos ;
        -Sort un programme permettant de dessiner le L-systems;
                                            """

"""
regles = {
    "A": "B",
    "B": "C"
}
axiom = "AB"
result = ""
for letter in axiom:
    if letter in regles:
        result += regles[letter]
    else:
        result += letter
print(result)
"""


def recup(x) :     # Fonction de récuparation des données du fichier
    stockage_info = {
        "axiome": None,
        "angle": None,
        "taille": None,
        "regles": {},
        "niveau": None
    }  # Espace de stockage des informatins (axiome, règles ect...)
    regle = False
    for line in x:
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


def crea (a,r) : #créa de l'axiome pour un niveau

    result = ""
    for letter in a:
        if letter in r:
            result += r[letter]
        else :
            result += letter
    return result


def creaniv (x,n,r) :
    result = ""
    for level in range (1 ,n):
        x = crea(x,r)
    return x










if __name__ == "__main__" :
    with open(input("Entrer le nom de votre fichier :")) as f : #Ouverture et lecture du fichier
        t = f.readlines()
        infos = recup(t) #application sur le fichier donné
        #print(infos)

         #def création de l'axiome
        axio = infos["axiome"]
        reg = infos["regles"]
        niv= infos["niveau"]
        axiorendu = crea(axio,reg)
        axiofinal = creaniv(axiorendu,niv,reg)
        print (axiofinal)
