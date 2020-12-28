import json
import datetime


item = dict()
itemMort = dict()
itemCas = dict()

def listeData(cheminJson):
    data_dict=dict()

    with open(cheminJson) as json_data:
        data_dict = json.load(json_data)

    liste = []
#on recupére les données dans une liste
    for cle in data_dict:
        liste.append(cle)
    return liste

#on extrait uniquement les données qui nous intérésse a savoir uniquement d'un pays passé en parmétre
def recherche_data_pays(pays):
    listedesdata=listeData('JSONData/data.json')
    for i in range(len(listedesdata)):
       item=listedesdata.__getitem__(i)
       if item["countriesAndTerritories"] == pays:
           json_object = json.dumps(item, indent=12)

    with open("JSONData/"+pays+".json", "w") as outfile:
               outfile.write(json_object)
    return outfile.name


#on extrait uniquement les données qui nous intérésse a savoir la date et le nombre de mort
def nbMortTotal(pays,date_debut,donnee):
    for i in range(len(donnee)):
       item=donnee.__getitem__(i)
       if item["countriesAndTerritories"]==pays:
          date=item["dateRep"]
          mort=item["deaths"]
          itemMort[date]=mort

    total =0
    for cle, valeur in itemMort.items():
        date = datetime.datetime.strptime(cle, '%d/%m/%Y')
        if date >= date_debut:
            total=total+valeur


    return total

#on extrait uniquement les données qui nous intérésse a savoir la date  et le nombre de cas
def nbCasTotal(pays,date_debut,donnee):
    for i in range(len(donnee)):
       item=donnee.__getitem__(i)
       if item["countriesAndTerritories"] == pays:
         date=item["dateRep"]
         cas=item["cases"]
         itemCas[date]=cas

    total = 0
    for cle, valeur in itemCas.items():
        date = datetime.datetime.strptime(cle, '%d/%m/%Y')
        if date >= date_debut:
            total=total+valeur


    return total

def moyenneDeCasParMois(pays,mois,moisFin,donnee):
    for i in range(len(donnee)):
       item=donnee.__getitem__(i)
       if item["countriesAndTerritories"] == pays:
         date=item["dateRep"]
         cas=item["cases"]
         itemCas[date]=cas
    labels = []
    data = []

    for cle, valeur in itemCas.items():

            labels.append(cle)
            data.append(valeur)
    somme = 0
    j = 0
    for i in range(len(labels)):
        date = datetime.datetime.strptime(labels.__getitem__(i), '%d/%m/%Y')
        if date>mois and date<moisFin:
           somme=somme+data.__getitem__(i)
           j=j+1

    moyenne=somme/j
    return moyenne
def casEnMoyenneParMois (pays):
    moyenne = []
    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 1, 1), datetime.datetime(2020, 1, 31),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 2, 1), datetime.datetime(2020, 2, 29),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 3, 1), datetime.datetime(2020, 3, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 4, 1), datetime.datetime(2020, 4, 30),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 5, 1), datetime.datetime(2020, 5, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 6, 1), datetime.datetime(2020, 6, 30),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 7, 1), datetime.datetime(2020, 7, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 8, 1), datetime.datetime(2020, 8, 31),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 9, 1), datetime.datetime(2020, 9, 30),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 10, 1), datetime.datetime(2020, 10, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 11, 1), datetime.datetime(2020, 11, 30),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDeCasParMois(pays, datetime.datetime(2020, 12, 1), datetime.datetime(2020, 12, 31),
                                         listeData('JSONData/data.json')))



    return moyenne,round(max(moyenne))


def moyenneDemortsParMois(pays,moisDebut,moisFin,donnee):
    for i in range(len(donnee)):
       item=donnee.__getitem__(i)
       if item["countriesAndTerritories"] == pays \
               and datetime.datetime.strptime(item["dateRep"], '%d/%m/%Y') >= datetime.datetime(2020, 1, 1):
         date=item["dateRep"]
         mort=item["deaths"]
         itemCas[date]=mort
    labels = []
    data = []

    for cle, valeur in itemCas.items():

            labels.append(cle)
            data.append(valeur)
    somme = 0
    j = 0
    for i in range(len(labels)):
        date = datetime.datetime.strptime(labels.__getitem__(i), '%d/%m/%Y')
        if date>moisDebut and date<moisFin:
           somme=somme+data.__getitem__(i)
           j=j+1

    moyenne=somme/j
    return moyenne
def mortEnMoyenneParMois(pays):
    moyenne = []
    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 1, 1), datetime.datetime(2020, 1, 31),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 2, 1), datetime.datetime(2020, 2, 29),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 3, 1), datetime.datetime(2020, 3, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 4, 1), datetime.datetime(2020, 4, 30),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 5, 1), datetime.datetime(2020, 5, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 6, 1), datetime.datetime(2020, 6, 30),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 7, 1), datetime.datetime(2020, 7, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 8, 1), datetime.datetime(2020, 8, 31),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 9, 1), datetime.datetime(2020, 9, 30),
                                         listeData('JSONData/data.json')))
    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 10, 1), datetime.datetime(2020, 10, 31),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 11, 1), datetime.datetime(2020, 11, 30),
                                         listeData('JSONData/data.json')))

    moyenne.append(moyenneDemortsParMois(pays, datetime.datetime(2020, 12, 1), datetime.datetime(2020, 12, 31),
                                         listeData('JSONData/data.json')))

    return moyenne,round(max(moyenne))