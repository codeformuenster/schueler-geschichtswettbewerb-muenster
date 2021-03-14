import mysql.connector
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField
import pandas as pd
import math

db = mysql.connector.connect(
    host="127.0.0.1",#"Richards-MBP-3.local",#"Richards-MacBook-Pro-3.local",
    user="root",
    passwd="LemanRuss1",
    database="gewe",#Put everything into gewe database
    auth_plugin='caching_sha2_password'
    #port="3306"
)

mycursor = db.cursor()


def enterSubmission(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor):
    #convert einzel_gruppe to boolean

    Q = 'INSERT INTO geweMap_beitrag (id, title, regest, sinatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor_id) VALUES (%d, %s, %s, %s, %s, %d, %d, %d, %d)'%(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis, tutor)
    mycursor.execute(Q)
    db.commit()

def enterSubmissionNoTut(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis):
    #convert einzel_gruppe to boolean

    Q = 'INSERT INTO geweMap_beitrag (id, title, regest, sinatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis) VALUES (%d, %s, %s, %s, %s, %d, %d, %d)'%(id, title, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis)
    mycursor.execute(Q)
    db.commit()

def enterPlace(id, ob, lat, lon):
    Q = 'INSERT INTO geweMap_ort (id, ortbezeichnung, location) Values (%d, %s, Point(%f, %f))'%(id, ob, lon, lat)
    mycursor.execute(Q)
    db.commit()

def enterPlaceSub(ort, beitr):
    Q = 'INSERT INTO geweMap_ort_beitraege (ort_id, beitrag_id) Values (%d, %d)'%(ort, beitr)
    mycursor.execute(Q)
    db.commit()

def enterAward(id, name):
    Q = 'INSERT INTO geweMap_auszeichnung (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterSchooltype(id, name):
    Q = 'INSERT INTO geweMap_schulart (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterSchool(id, name):
    Q = 'INSERT INTO geweMap_schule (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterScholSchooltype(school, type):
    Q = 'INSERT INTO geweMap_schuleschulart (art_id, schule_id) Values (%d, %d)'%(type, school)
    mycursor.execute(Q)
    db.commit()

def enterWettbewerb(id, topic, shortTitle, year, summary):
    Q = 'INSERT INTO geweMap_wettbewerb (id, topic, shortTitle, year, summary) Values (%d, %s, %s, %s, %s)'%(id, topic, shortTitle, year, summary)
    mycursor.execute(Q)
    db.commit()

def enterMg(id, name):
    Q = 'INSERT INTO geweMap_materialgrundlage (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterDT(id, name):
    Q = 'INSERT INTO geweMap_dokumenttyp (id, typName) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterTutor(id, code):
    Q = 'INSERT INTO geweMap_tutor (id, code) Values (%d, %s)'%(id, code)
    mycursor.execute(Q)
    db.commit()

def enterPerson(id, name):
    Q = 'INSERT INTO geweMap_persoenlichkeit (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitrart(id, name):
    Q = 'INSERT INTO geweMap_beitragsart (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitragWettbewerb(bid, wid):
    Q = 'INSERT INTO geweMap_beitragWettbewerb (beitrag_id, wettbewerb_id) Values (%d, %d)'%(bid, wid)
    mycursor.execute(Q)
    db.commit()

def enterAutorin(id, fname, sname, beitrID):
    Q = 'INSERT INTO geweMap_autorin (id, firstname, surname, beitrag_id) Values (%d, %s, %s, %d)'%(id, fname, sname, beitrID)
    mycursor.execute(Q)
    db.commit()

def enterAutSch(autID, sID, grade):
    Q = 'INSERT INTO geweMap_autorinschule (autorin_id, schule_id, grade) Values (%d, %d, %d)'%(autID, sID, grade)
    mycursor.execute(Q)
    db.commit()

def enterAuszEinr(bID, aID):
    Q = 'INSERT INTO geweMap_auszeichnungeinreichung (auszeichnung_id, einreichung_id) Values (%d, %d)'%(aID, bID)
    mycursor.execute(Q)
    db.commit()

def enterHistPlace(id, name):
    Q = 'INSERT INTO geweMap_historicplace (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterHistReg(id, name):
    Q = 'INSERT INTO geweMap_historicregion (id, name) Values (%d, %s)'%(id, name)
    mycursor.execute(Q)
    db.commit()

def enterBeitPers(bID, pID):
    Q = 'INSERT INTO geweMap_beitrag_persoenlichkeiten (beitrag_id, persoenlichkeit_id) Values (%d, %d)'%(bID, pID)
    mycursor.execute(Q)
    db.commit()

def enterBeitrArt(bID, baID):
    Q = 'INSERT INTO geweMap_beitrag_typ(beitrag_id, beitragsart_id) Values (%d, %d)'%(bID, baID)
    mycursor.execute(Q)
    db.commit()

def enterOrtHist(oID, hpID):
    Q = 'INSERT INTO geweMap_ort_histName(ort_id, historicplace_id) Values (%d, %d)'%(oID, hpID)
    mycursor.execute(Q)
    db.commit()

def enterOrtRegion(oID, hrID):
    Q = 'INSERT INTO geweMap_ort_histRegion(ort_id, historicregion_id) Values (%d, %d)'%(oID, hrID)
    mycursor.execute(Q)
    db.commit()

x = pd.read_excel('/Users/richardalbrecht/Desktop/GeweXlsxTabellen/OrtHistreg.xlsx').to_numpy()
#'/Users/richardalbrecht/Desktop/GeweXlsxTabellen/Beitragsort.xlsx').to_numpy()
#'/Users/richardalbrecht/Desktop/BA/BA Dokumente/csvTabellen/KoordinatenTest.xlsx').to_numpy()

Q = 'UPDATE geweMap_ort Set location=Point(%f,%f) Where id=179'%(104.869, 13.5066)
mycursor.execute(Q)
db.commit()
#for i in range (1, len(x)):
    #print(x[i])
    #enterHistPlace(x[i][0], ("\"" + x[i][1] + "\""))
    #enterOrtRegion(x[i][0], x[i][1])
    #enterPlace(179, ("\"" + Kambodscha + "\""), 104.869, 13.5066)

    #if math.isnan(float(x[i][2])) == False:
        #enterPlace(int(x[i][0]), ("\""+ x[i][1] + "\""), float(x[i][3]), float(x[i][2]))
    #else:
        #enterPlace(int(x[i][0]), ("\""+ x[i][1] + "\""), 0.0, 0.0)
    #if math.isnan(float(x[i][2])) == False:
    #    enterAutSch(int(x[i][0]), int(x[i][1]), int(x[i][2]))
    #else:
    #    enterAutSchNoGrade(int(x[i][0]), int(x[i][1]))
    #enterAuszEinr(x[i][0], x[i][1])
    #enterAutorin(x[i][0], ("\"" + str(x[i][1]) + "\""), ("\"" + str(x[i][2]) + "\""), x[i][3])
    #if math.isnan(float(x[i][8])) == False:
    #    enterSubmission(int(x[i][0]),
    #    ("\"" + str(x[i][1]) + "\""),
    #    "\"" + x[i][2] + "\"", ("\"" + x[i][3] + "\""),
    #    x[i][4],
    #    int(x[i][5]),
    #    int(x[i][6]),
    #    int(x[i][7]),
    #    int(x[i][8]))
    #else:
    #    enterSubmissionNoTut(int(x[i][0]),
    #    ("\"" + str(x[i][1]) + "\""),
    #    "\"" + x[i][2] + "\"", ("\"" + x[i][3] + "\""),
    #    x[i][4],
    #    int(x[i][5]),
    #    int(x[i][6]),
    #    int(x[i][7]))
    #printx[i]
    #enterPlaceSub(int(x[i][1]), int(x[i][0]))
    #enterPlace(int(x[i][0]), ("\""+ x[i][1] + "\""), float(x[i][5]), float(x[i][6]))


#Q = 'INSERT INTO geweMap_beitrag (id, title, regest, sinatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis) VALUES (%d, %s, %s, \"c\", %r, 1, 2, 3)'%(int(x[1][0]), ("\"" + str(x[1][1]) + "\""), ("\"" + str(x[1][2]) + "\""), True)
#Q = 'INSERT INTO geweMap_ort_beitraege (ort_id, beitrag_id) Values (%d, %d)'%(178, 1)
#mycursor.execute(Q)
#db.commit()

    #if x[i][5] != 'nan':
        #print(x[i][1] + '...' + x[i][5] + '...' + x[i][6])

#Insert into geweTest.geweMap_ort (ortbezeichnung, location) values ("insertTest", Point(0, 0));
#alter table geweTest.geweMap_ort auto_increment = 1;
