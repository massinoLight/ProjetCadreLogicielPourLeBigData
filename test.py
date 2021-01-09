import os
import pycountry

if __name__ == "__main__":
    paysArg=""

    for country in pycountry.countries:
        paysArg=paysArg+" "+country.alpha_3

    dernier = os.system("java -jar ./hive.jar "+paysArg)



