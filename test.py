import os
import pycountry
############################################################
#      permet de générer le fichier monde.json              #
# a partir de Hive qui va exécuter le traitement de la req #
############################################################


if __name__ == "__main__":
    paysArg=""

    for country in pycountry.countries:
        paysArg=paysArg+" "+country.alpha_3

    dernier = os.system("java -jar ./hive.jar "+paysArg)



