import mysql.connector
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField
import pandas as pd
import math

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="geschichtswettbewerb",
    auth_plugin='caching_sha2_password'
)

mycursor = db.cursor()
#There is a function for every database table to enter the data.
def enterSubmission(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor):
    Q = 'INSERT INTO karte_beitrag (id, titel, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor_id) VALUES (%d, %s, %s, %s, %s, %d, %d, %d, %d)'%(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor)
    mycursor.execute(Q)
    db.commit()

def enterSubmissionNoTut(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis):
    Q = 'INSERT INTO karte_beitrag (id, titel, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis) VALUES (%d, %s, %s, %s, %s, %d, %d, %d)'%(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis)
    mycursor.execute(Q)
    db.commit()

def enterPlace(id, ob, lat, lon):
    Q = 'INSERT INTO karte_ort (id, ortbezeichnung, location) Values (%d, %s, Point(%f, %f))'%(id, ob, lon, lat)
    mycursor.execute(Q)
    db.commit()

def enterPlaceSub(ort, beitr):
    Q = 'INSERT INTO karte_ort_beitraege (ort_id, beitrag_id) Values (%d, %d)'%(ort, beitr)
    mycursor.execute(Q)
    db.commit()

def enterAward(id, name):
    Q = 'INSERT INTO karte_auszeichnung (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterSchooltype(id, name):
    Q = 'INSERT INTO karte_schulart (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterSchool(id, name):
    Q = 'INSERT INTO karte_schule (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterScholSchooltype(school, type):
    Q = 'INSERT INTO karte_schuleschulart (art_id, schule_id) Values (%d, %d)'%(type, school)
    mycursor.execute(Q)
    db.commit()

def enterWettbewerb(id, topic, shortTitle, year, summary):
    Q = 'INSERT INTO karte_wettbewerb (id, thema, kurztitel, jahr, zusammenfassung) Values (%d, %s, %s, %s, %s)'%(id, topic, shortTitle, year, summary)
    mycursor.execute(Q)
    db.commit()

def enterMg(id, name):
    Q = 'INSERT INTO karte_materialgrundlage (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterDT(id, name):
    Q = 'INSERT INTO karte_dokumenttyp (id, typName) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterTutor(id, code):
    Q = 'INSERT INTO karte_tutor (id, code) Values (%d, %s)'%(id, code)
    mycursor.execute(Q)
    db.commit()

def enterPerson(id, name):
    Q = 'INSERT INTO karte_persoenlichkeit (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitrart(id, name):
    Q = 'INSERT INTO karte_beitragsart (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitragWettbewerb(bid, wid):
    Q = 'INSERT INTO karte_beitragWettbewerb (beitrag_id, wettbewerb_id) Values (%d, %d)'%(bid, wid)
    mycursor.execute(Q)
    db.commit()

def enterAutorin(id, fname, sname, beitrID):
    Q = 'INSERT INTO karte_autorin (id, vorname, nachname, beitrag_id) Values (%d, %s, %s, %d)'%(id, fname, sname, beitrID)
    mycursor.execute(Q)
    db.commit()

def enterAutSch(autID, sID, grade):
    Q = 'INSERT INTO karte_autorinschule (autorin_id, schule_id, jahrgangsstufe) Values (%d, %d, %d)'%(autID, sID, grade)
    mycursor.execute(Q)
    db.commit()

def enterAutSchNoGrade(autID, sID):
    Q = 'INSERT INTO karte_autorinschule (autorin_id, schule_id) Values (%d, %d)'%(autID, sID)
    mycursor.execute(Q)
    db.commit()

def enterAuszEinr(bID, aID):
    Q = 'INSERT INTO karte_auszeichnungeinreichung (auszeichnung_id, einreichung_id) Values (%d, %d)'%(aID, bID)
    mycursor.execute(Q)
    db.commit()

def enterHistPlace(id, name):
    Q = 'INSERT INTO karte_historischerort (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterHistReg(id, name):
    Q = 'INSERT INTO karte_historischeregion (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitPers(bID, pID):
    Q = 'INSERT INTO karte_beitrag_persoenlichkeiten (beitrag_id, persoenlichkeit_id) Values (%d, %d)'%(bID, pID)
    mycursor.execute(Q)
    db.commit()

def enterBeitrArt(bID, baID):
    Q = 'INSERT INTO karte_beitrag_typ(beitrag_id, beitragsart_id) Values (%d, %d)'%(bID, baID)
    mycursor.execute(Q)
    db.commit()

def enterOrtHist(oID, hpID):
    Q = 'INSERT INTO karte_ort_histName(ort_id, historischerort_id) Values (%d, %d)'%(oID, hpID)
    mycursor.execute(Q)
    db.commit()

def enterOrtRegion(oID, hrID):
    Q = 'INSERT INTO karte_ort_histRegion(ort_id, historischeregion_id) Values (%d, %d)'%(oID, hrID)
    mycursor.execute(Q)
    db.commit()

def enterBeitrGrundlagen(bID, mgID):
    Q = 'INSERT INTO karte_beitrag_grundlagen(beitrag_id, materialgrundlage_id) Values (%d, %d)'%(bID, mgID)
    mycursor.execute(Q)
    db.commit()
