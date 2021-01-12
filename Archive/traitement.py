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

l=listeData("JSONData/monde.json")



"""
fonction qui va attribuer un score entre 0 et 100 selon la gravité du pays 
"""

def score(l):
    #l = listeData("JSONData/Europe.json")
    isoCode = []
    indicateur = []
    size = []
    indice = 0
    taille = 0;
    for item in l:
        indice = 0
        isoCode.append(item['Code pays'])


        if item['Nombre d\'hospitalisation en moyenne']!=None:
           if float(item['Nombre d\'hospitalisation en moyenne']) > 30000:
             indice = indice + 25

        if item['Moyenne d\'age']!=None:
           if float(item['Moyenne d\'age'])>40:
             indice=indice+20

        if item['Moyenne des morts']!=None:
           if float(item['Moyenne des morts'])>200:
              indice = indice + 20

        if  item['Moyenne des cas']!=None:
          if float(item['Moyenne des cas'])>8000:
              indice = indice + 30

        if item['Nombre de tests en moyenne']!=None:
          if float(item['Nombre de tests en moyenne'])<30000:
                 indice = indice + 25

        indicateur.append(indice)
    return  indicateur



def isoCode(l):
    isoCode = []
    for item in l:
        isoCode.append(item['Code pays'])
    return isoCode


def mortMoyenne(l):
    moyenne_mort = []
    for item in l:
        moyenne_mort.append(item['Moyenne des morts'])
    return moyenne_mort

def casMoyenne(l):
    moyenne_cas = []
    for item in l:
        moyenne_cas.append(item['Moyenne des cas'])
    return moyenne_cas


def hospitalisation(l):
    moyenne_hospitalisation = []
    for item in l:
        moyenne_hospitalisation.append(item['Nombre d\'hospitalisation en moyenne'])
    return moyenne_hospitalisation

def ageMoyen(l):
    moyenne_age = []
    for item in l:
        moyenne_age.append(item['Moyenne d\'age'])
    return moyenne_age

def testMoyen(l):
    moyenne_test = []
    for item in l:
        moyenne_test.append(item['Nombre de tests en moyenne'])
    return moyenne_test


"""for item in l:
    print(item ['Code pays'])
    print("Hospitalisation "+str(item['Nombre d\'hospitalisation en moyenne']))
    print("test moyenne "+str(item['Nombre de tests en moyenne']))
    print("age moyen "+str(item['Moyenne d\'age']))
    print("cas moyenne "+str(item['Moyenne des cas']))
    print("morts "+str(item['Moyenne des morts']))
    print("***********************")"""