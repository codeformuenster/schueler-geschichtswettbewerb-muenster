import mysql.connector
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField
import pandas as pd
import math

db = mysql.connector.connect(
    host="127.0.0.1",
    user="website",
    passwd="SarmatiaEuropaca1*",
    database="geweNewDump",
    auth_plugin='caching_sha2_password'
)

mycursor = db.cursor()
"""There is a function for every database table to enter data with the given columns as parameters"""

"""read the file from which the data is to be entered"""
data = pd.read_excel('beitrag_jahrgangsstufe.xlsx').to_numpy()

def enterSubmission(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor):
    """Enter submissions with a tutor"""
    Q = 'INSERT INTO karte_beitrag (id, titel, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor_id) VALUES (%d, %s, %s, %s, %s, %d, %d, %d, %d)'%(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor)
    mycursor.execute(Q)
    db.commit()

def enterSubmissionNoTut(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis):
    """Enter submissions without a tutor"""
    Q = 'INSERT INTO karte_beitrag (id, titel, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis) VALUES (%d, %s, %s, %s, %s, %d, %d, %d)'%(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis)
    mycursor.execute(Q)
    db.commit()

def enterPlace(id, ob, lat, lon):
    """Enter places with name ob, latitude and longitude"""
    Q = 'INSERT INTO karte_ort (id, ortbezeichnung, location) Values (%d, %s, Point(%f, %f))'%(id, ob, lon, lat)
    mycursor.execute(Q)
    db.commit()

def enterPlaceSub(ort, beitr):
    """Enter place id ort and submission id beitr to karte_ort_beitraege"""
    Q = 'INSERT INTO karte_ort_beitraege (ort_id, beitrag_id) Values (%d, %d)'%(ort, beitr)
    mycursor.execute(Q)
    db.commit()

def enterAward(id, name):
    """Enter award entries with id and name"""
    Q = 'INSERT INTO karte_auszeichnung (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterSchooltype(id, name):
    """Enter schooltypes with id and name"""
    Q = 'INSERT INTO karte_schulart (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterSchool(id, name):
    """Enter schools with id and name"""
    Q = 'INSERT INTO karte_schule (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterScholSchooltype(school, type):
    """Enter the relation of school and schooltype with schooltype id and school id"""
    Q = 'INSERT INTO karte_schuleschulart (art_id, schule_id) Values (%d, %d)'%(type, school)
    mycursor.execute(Q)
    db.commit()

def enterWettbewerb(id, topic, shortTitle, year, summary):
    """Enter competitions with a topic, shortTitle, starting year and a summary"""
    Q = 'INSERT INTO karte_wettbewerb (id, thema, kurztitel, jahr, zusammenfassung) Values (%d, %s, %s, %s, %s)'%(id, topic, shortTitle, year, summary)
    mycursor.execute(Q)
    db.commit()

def enterMg(id, name):
    """Enter source materials with id and name"""
    Q = 'INSERT INTO karte_materialgrundlage (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterDT(id, name):
    """Enter document types with id and name"""
    Q = 'INSERT INTO karte_dokumenttyp (id, typName) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterTutor(id, code):
    """Enter tutors with id and code"""
    Q = 'INSERT INTO karte_tutor (id, code) Values (%d, %s)'%(id, code)
    mycursor.execute(Q)
    db.commit()

def enterPerson(id, name):
    """Enter persons with id and name"""
    Q = 'INSERT INTO karte_persoenlichkeit (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitrart(id, name):
    """Enter submission types with id and name"""
    Q = 'INSERT INTO karte_beitragsart (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitragWettbewerb(bid, wid):
    """Enter persons with id and name"""
    Q = 'INSERT INTO karte_beitragWettbewerb (beitrag_id, wettbewerb_id) Values (%d, %d)'%(bid, wid)
    mycursor.execute(Q)
    db.commit()

def enterAutorin(id, fname, sname, beitrID):
    """Enter authors with id, first name, surname and the submission id"""
    Q = 'INSERT INTO karte_autorin (id, vorname, nachname, beitrag_id) Values (%d, %s, %s, %d)'%(id, fname, sname, beitrID)
    mycursor.execute(Q)
    db.commit()

def enterAutSch(autID, sID, grade):
    """Enter the relation for authors and schools with author_id, school_id and the authors grade"""
    Q = 'INSERT INTO karte_autorinschule (autorin_id, schule_id, jahrgangsstufe) Values (%d, %d, %d)'%(autID, sID, grade)
    mycursor.execute(Q)
    db.commit()

def enterAutSchNoGrade(autID, sID):
    """Enter the relation for authors and schools with author_id, school_id without the authors grade"""
    Q = 'INSERT INTO karte_autorinschule (autorin_id, schule_id) Values (%d, %d)'%(autID, sID)
    mycursor.execute(Q)
    db.commit()

def enterAuszEinr(bID, aID):
    """Enter the relation for submissions and awards with a submission_id and award_id"""
    Q = 'INSERT INTO karte_auszeichnungeinreichung (auszeichnung_id, einreichung_id) Values (%d, %d)'%(aID, bID)
    mycursor.execute(Q)
    db.commit()

def enterHistPlace(id, name):
    """Enter historical places with id and name"""
    Q = 'INSERT INTO karte_historischerort (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterHistReg(id, name):
    """Enter historical regions with id and name"""
    Q = 'INSERT INTO karte_historischeregion (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitPers(bID, pID):
    """Enter the relation between persons and submissions with submission_id and person_id"""
    Q = 'INSERT INTO karte_beitrag_persoenlichkeiten (beitrag_id, persoenlichkeit_id) Values (%d, %d)'%(bID, pID)
    mycursor.execute(Q)
    db.commit()

def enterBeitrArt(bID, baID):
    """Enter the relation between submissions and submission types with submission_id and submission type_id"""
    Q = 'INSERT INTO karte_beitrag_typ(beitrag_id, beitragsart_id) Values (%d, %d)'%(bID, baID)
    mycursor.execute(Q)
    db.commit()

def enterOrtHist(oID, hpID):
    """Enter the relation between places and hisorical places with place_id and historical_place_id"""
    Q = 'INSERT INTO karte_ort_histName(ort_id, historischerort_id) Values (%d, %d)'%(oID, hpID)
    mycursor.execute(Q)
    db.commit()

def enterOrtRegion(oID, hrID):
    """Enter the relation between places and hisorical regions with place_id and historical_region_id"""
    Q = 'INSERT INTO karte_ort_histRegion(ort_id, historischeregion_id) Values (%d, %d)'%(oID, hrID)
    mycursor.execute(Q)
    db.commit()

def enterBeitrGrundlagen(bID, mgID):
    """Enter the relation between submissions and source materials with submission_id and source_material_id"""
    Q = 'INSERT INTO karte_beitrag_grundlagen(beitrag_id, materialgrundlage_id) Values (%d, %d)'%(bID, mgID)
    mycursor.execute(Q)
    db.commit()

def enterSubmissionGrade(bID, grade):
    """Enter the relation between submissions and source materials with submission_id and grade_id"""
    Q = 'INSERT INTO karte_beitrag_jahrgaenge (beitrag_id, jahrgangsstufe_id) Values (%d, %d)'%(bID, grade)
    mycursor.execute(Q)
    db.commit()

def enterGrades(grade):
    """enter a new grade to the table jahrgangsstufe"""
    Q = 'INSERT INTO karte_jahrgangsstufe (id, stufe) Values (%d, %d)'%(grade, grade)
    mycursor.execute(Q)
    db.commit()

#print(data[0][0], len(data))
#for i in range(0, len(data)):
#    print(math.isnan(float(data[i][1])), "NEXT", i)
#    if(math.isnan(float(data[i][1])) == False):
#        enterSubmissionGrade(int(data[i][0]), int(data[i][1]))
