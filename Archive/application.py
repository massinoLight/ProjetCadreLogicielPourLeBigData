from flask import Flask, Markup, render_template,request
from covid_19 import nbCasTotal, nbMortTotal, listeData, casEnMoyenneParMois, mortEnMoyenneParMois
from traitement import *
import datetime

application = Flask(__name__)


labels = [
    "Janvier", "Février", "Mars", "Avril",
    "Mai", "Juin", "Juillet", "Aout",
    "Septembre", "Octobre", "Décembre"]


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]



@application.route('/line', methods=["GET", "POST"])
def line():
    Pays= request.form['country']
    line_labels=labels
    line_values,max1=mortEnMoyenneParMois(Pays)
    line_values2,max2 = casEnMoyenneParMois(Pays)
    totCAs=nbCasTotal(Pays, datetime.datetime(2020, 1, 1), listeData('JSONData/covidData.json'))
    totMort=nbMortTotal(Pays, datetime.datetime(2020, 1, 1), listeData('JSONData/covidData.json'))
    return render_template('line_chart.html', title='Moyenne de mort par la Covid 19 par mois in '+ Pays,
                           title2='Moyenne des cas Covid 19 par moi in '+ Pays,
                           max=max1, labels=line_labels, values=line_values,max2=max2,values2=line_values2,
                           toalCas=totCAs,toalMort=totMort)

@application.route('/', methods=["GET", "POST"])
def envoyer():
    return render_template('index.html')

@application.route('/pays', methods=['GET', 'POST'])
def pays():
    return render_template('pays.html')

@application.route('/afrique', methods=['GET', 'POST'])
def afrique():
    l = listeData("JSONData/Afrique.json")
    sc=score(l)
    iso=isoCode(l)
    m = mortMoyenne(l)
    cas = casMoyenne(l)
    h = hospitalisation(l)
    a = ageMoyen(l)
    t = testMoyen(l)


    return render_template('map.html', continent='africa',codepays=iso,scoring=sc,mort=m,cas=cas,hospitalisation=h,age=a,test=t)

@application.route('/ameriqueNord', methods=['GET', 'POST'])
def ameriqueNord():
    l = listeData("JSONData/North America.json")
    sc = score(l)
    iso = isoCode(l)
    m = mortMoyenne(l)
    cas = casMoyenne(l)
    h = hospitalisation(l)
    a = ageMoyen(l)
    t = testMoyen(l)
    return render_template('map.html', continent='north america', codepays=iso, scoring=sc,mort=m,cas=cas,hospitalisation=h,age=a,test=t)

@application.route('/ameriqueSud', methods=['GET', 'POST'])
def ameriqueSud():
    l = listeData("JSONData/South America.json")
    sc = score(l)
    iso = isoCode(l)
    m = mortMoyenne(l)
    cas = casMoyenne(l)
    h = hospitalisation(l)
    a = ageMoyen(l)
    t = testMoyen(l)
    return render_template('map.html', continent='south america', codepays=iso, scoring=sc,mort=m,cas=cas,hospitalisation=h,age=a,test=t)

@application.route('/asie', methods=['GET', 'POST'])
def asie():
    l = listeData("JSONData/Asie.json")
    sc = score(l)
    iso = isoCode(l)
    m = mortMoyenne(l)
    cas = casMoyenne(l)
    h = hospitalisation(l)
    a = ageMoyen(l)
    t = testMoyen(l)

    return render_template('map.html', continent='asia', codepays=iso, scoring=sc,mort=m,cas=cas,hospitalisation=h,age=a,test=t)

@application.route('/europe', methods=['GET', 'POST'])
def europe():
    l = listeData("JSONData/Europe.json")
    sc = score(l)
    iso = isoCode(l)
    m = mortMoyenne(l)
    cas=casMoyenne(l)
    h=hospitalisation(l)
    a=ageMoyen(l)
    t=testMoyen(l)
    return render_template('map.html', continent='europe', codepays=iso, scoring=sc,mort=m,cas=cas,hospitalisation=h,age=a,test=t)


@application.route('/monde', methods=['GET', 'POST'])
def monde():
    l = listeData("JSONData/monde.json")
    sc = score(l)
    iso = isoCode(l)
    m = mortMoyenne(l)
    cas = casMoyenne(l)
    h = hospitalisation(l)
    a = ageMoyen(l)
    t = testMoyen(l)
    comb=zip(h,m)
    return render_template('map.html' , continent='world', codepays=iso, scoring=sc,mort=m,cas=cas,hospitalisation=h,age=a,test=t,combiner=comb)