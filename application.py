import random
import time
import os
from flask import Flask, Markup, render_template,request
from covid_19 import nbCasTotal, nbMortTotal, listeData, casEnMoyenneParMois, mortEnMoyenneParMois
from traitement import *
import datetime
from twitter import *

application = Flask(__name__)


labels = [
    "Janvier", "Février", "Mars", "Avril",
    "Mai", "Juin", "Juillet", "Aout",
    "Septembre", "Octobre", "Décembre"]


colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]



OAUTH_TOKEN="1348441876685344775-4FGcZIDUnoMeRM48sKPcLAKcgRMlFn"
OAUTH_SECRET="goLSFOD43UHPM7bHpuFpryrpeOBv7Jz6IkNH0ASIxEFJx"
CONSUMER_KEY="bSAL2fgRBaXLYp4hua5ZVfVX9"
CONSUMER_SECRET="EnZRCCgMI32E9QOQu9Z4YXEK7Ou5jdlzWvGiqHg4I0G3m0dp4q"

leTwitts=["SantePubliqueFr","olivierveran","CoronaNumbers","EmmanuelMacron"]
r=random.randint(0, 2)

twitter = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)

           )



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

    myTweets = twitter.statuses.user_timeline(count=4)

    # fetch 3 random tweets de la liste des twitters precedente
    itpTweets = twitter.statuses.user_timeline(screen_name=leTwitts.__getitem__(r), count=4)


    templateData = {
        'title': 'tweets Corona virus',
        'myTweets': myTweets,
        'itpTweets': itpTweets
    }

    return render_template('index.html', **templateData)

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



@application.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# This is a jinja custom filter
@application.template_filter('strftime')
def _jinja2_filter_datetime(date, fmt=None):
    pyDate = time.strptime(date,'%a %b %d %H:%M:%S +0000 %Y') # convert twitter date string into python date/time
    return time.strftime('%Y-%m-%d %H:%M:%S', pyDate) # return the formatted date.