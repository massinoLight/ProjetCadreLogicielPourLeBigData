import json
"""
scope (enumerated: "world" | "usa" | 
"europe" | "asia" | "africa" | "north america" | 
"south america" ) default: "world"
"""

item = dict()
itemMort = dict()
itemCas = dict()

def listeData(chemin):
    data_dict=dict()

    with open(chemin) as json_data:
        data_dict = json.load(json_data)

    liste = []
#on recupére les données dans une liste
    for cle in data_dict:
        liste.append(cle)
    return liste

"""l=listeData("JSONData/Europe.json")

for item in l:
    print(item ['Code pays'])
    print("Hospitalisation "+str(item['Nombre d\'hospitalisation en moyenne']))
    print("test moyenne "+str(item['Nombre de tests en moyenne']))
    print("age moyen "+str(item['Moyenne d\'age']))
    print("cas moyenne "+str(item['Moyenne des cas']))
    print("morts "+str(item['Moyenne des morts']))
    print("***********************")"""


def score():
    l = listeData("JSONData/Europe.json")
    isoCode = []
    indicateur = []
    size = []
    indice = 0
    taille = 0;
    for item in l:
        isoCode.append(item['Code pays'])
        if item['Nombre d\'hospitalisation en moyenne'] > 30000:
            indice = indice + 20
            if item['Moyenne d\'age']>40:
                indice=indice+20
                if item['Moyenne des morts']>200:
                   indice = indice + 20
                    if item['Moyenne des cas']>8000 or item['Nombre de tests en moyenne']<30000:
                        indice = indice + 20

        indicateur.append(indice)


