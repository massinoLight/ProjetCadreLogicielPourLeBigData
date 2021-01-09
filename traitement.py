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

l=listeData("JSONData/Europe.json")

for item in l:
    print(item)