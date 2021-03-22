import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="geschichtswettbewerb",
    auth_plugin='caching_sha2_password'
)

mycursor = db.cursor()

#A class that contains methods to execute all required queries and prints them to the command line.
class Query:

    #Print a cursor object.
    def printCursor(self, cursor):
        for x in cursor:
            print(x)

    #Get the count of any query
    def queryCount(self, cursor):
        print(cursor.rowcount)


    #Get all authors with their respective submissions.
    def autorinBeitrag(self):
        Q = "SELECT b.id, b.signatur, a.vorname, a.nachname, a.id FROM karte_beitrag b INNER JOIN karte_autorin a ON a.beitrag_id=b.id"
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor
    #autorinBeitrag()

    ####################################
    #1 Content
    ####################################

    #Query for submissions that write about the time period from x to y
    def beitrFromTo(self, x, y):
        Q = "SELECT b.id, b.titel FROM karte_beitrag b WHERE zeitraumVon >= %d AND zeitraumBis <= %d" %(x, y)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Select Beitrag to a place p dealing with the years x to y
    def beitragPlace(self, p, x = 0, y = 2020):
        Q = "SELECT o.ortbezeichnung, o.id, b.id, b.titel FROM ((karte_ort_beitraege bo INNER JOIN karte_ort o ON o.id=bo.ort_id) INNER JOIN karte_beitrag b ON bo.beitrag_id=b.id) WHERE ortbezeichnung=\"%s\" AND zeitraumVon>=%d AND zeitraumBis<=%d" %(p, x, y)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions that are about person pers.
    def beitragPerson(self, pers):
        Q = "SELECT b.id, b.titel, p.name, p.id FROM ((karte_beitrag_persoenlichkeiten bp INNER JOIN karte_persoenlichkeit p ON bp.persoenlichkeit_id=p.id) INNER JOIN karte_beitrag b ON b.id=bp.beitrag_id) WHERE p.name=\"%s\""%(pers)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Returns all submissions about a given place (place) and person (pers).
    def ortPers(self, place, pers):
        Q = "SELECT b.id, b.titel, p.name, p.id, o.ortbezeichnung, o.id FROM (((karte_ort_beitraege bo INNER JOIN karte_ort o ON bo.ort_id=o.id) INNER JOIN karte_beitrag b ON b.id=bo.beitrag_id) INNER JOIN (karte_beitrag_persoenlichkeiten bp INNER JOIN karte_persoenlichkeit p ON bp.persoenlichkeit_id=p.id) ON bp.beitrag_id=bo.beitrag_id) WHERE o.ortbezeichnung=\"%s\" AND p.name=\"%s\""%(place, pers)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions handed in at competition with title w.
    def beitrWett(self, w):
        Q = "SELECT b.id, b.titel, w.id, w.thema FROM ((karte_beitragwettbewerb bw INNER JOIN karte_beitrag b ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.thema=\"%s\"" %(w)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions handed in to competition w dealing with place o.
    def wettOrt(self, w, o):
        Q = "SELECT b.id, b.titel, w.id, w.thema, o.ortbezeichnung, bo.ort_id FROM ((((karte_ort_beitraege bo INNER JOIN karte_ort o ON o.id=bo.ort_id) INNER JOIN karte_beitrag b ON bo.beitrag_id=b.id) INNER JOIN karte_beitragwettbewerb bw ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.thema=\"%s\" AND o.ortbezeichnung=\"%s\""%(w, o)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions with tutors of competition year x
    def tutJahr(self, x):
        Q = "SELECT b.id, b.titel, w.thema, w.id FROM ((karte_beitragwettbewerb bw INNER JOIN karte_beitrag b ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE b.tutor_id>0 AND w.jahr=%d"%(x)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions from authors of grade js and submission year jahr.
    def tutJahrgang(self, js, jahr):
        Q = "SELECT b.id, b.titel FROM ((((karte_beitrag b INNER JOIN karte_beitragwettbewerb wb ON b.id=wb.beitrag_id)INNER JOIN karte_wettbewerb w ON w.id=wb.wettbewerb_id)) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE aus.jahrgangsstufe=%d AND w.jahr=%d"%(js, jahr)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions with source material x.
    def mGrundlage(self, x):
        Q = "SELECT b.id, b.titel, mg.name, mg.id FROM ((karte_beitrag b INNER JOIN karte_beitrag_grundlagen bg ON b.id=bg.beitrag_id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE mg.name=\"%s\""%(x)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions of a certain type bta submitted at competition year jahr.
    def mgJahr(self, bta, jahr):
        Q = "SELECT b.id, b.titel, w.jahr, w.id FROM (((karte_beitrag b INNER JOIN karte_beitrag_typ bba ON b.id=bba.beitrag_id) INNER JOIN karte_beitragsart ba ON ba.id=bba.beitragsart_id) INNER JOIN (karte_beitragwettbewerb bw INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) ON bw.beitrag_id=b.id) WHERE ba.name=%s AND w.jahr=%d"%(bta, jahr)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submission with given type bta and source material mgr
    def baBgr(self, bta, mgr):
        Q = "SELECT ba.name, mg.name, b.titel, b.id FROM (((((karte_beitrag b INNER JOIN karte_beitrag_typ bba ON b.id=bba.beitrag_id) INNER JOIN karte_beitragsart ba ON ba.id=bba.beitragsart_id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=b.id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id)) WHERE ba.name=\"%s\" AND mg.name=\"%s\""%(bta,mgr)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions that received awards.
    def bAusz(self):
        Q = "SELECT b.id, b.titel, a.name FROM ((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON b.id=ea.einreichung_id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) WHERE ea.id>0"
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    #Submissions about a place o using source material mgr.
    def ortMG(self, o, mgr):
        Q = "SELECT b.id, b.titel, o.ortbezeichnung, mg.name FROM ((((karte_beitrag b INNER JOIN karte_ort_beitraege bo ON b.id=bo.beitrag_id) INNER JOIN karte_ort o ON o.id=bo.ort_id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=bo.beitrag_id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE o.ortbezeichnung=\"%s\" AND mg.name=\"%s\""%(o,mgr)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    #Submissions that are about a certain topic t. The topic is searched within the title and regest of the submissions.
    def beitrThema(self, t):
        Q = "SELECT b.id, b.titel FROM karte_beitrag b WHERE b.titel LIKE \"%" + t + "%\" OR b.regest LIKE \"%" + t + "%\""
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    ###################
    #2 Working methods
    ###################

    #Submissions from authors in grade jVon to jBis woking allone (grp="True") or in a group (grp="False")
    def grpJahrg(self, jVon, jBis, grp):
        Q = "SELECT b.id, b.titel, aus.jahrgangsstufe, b.einzel_gruppe FROM ((karte_beitrag b INNER JOIN karte_autorin a ON a.beitrag_id=b.id) INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) WHERE b.einzel_gruppe=%d AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d"%(grp, jVon, jBis)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Beitraege aus Jahrgaengen mit dokumenttyp
    def dtbeitrJahrg(self, dt, jVon, jBis):
        Q = "SELECT Distinct b.id, b.titel, aus.jahrgangsstufe FROM (((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE dt.typName=\"%s\" AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d"%(dt, jVon, jBis)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions from students in grades from jVon to jBis who worked allown or in a group (grp) containing a work report or tutor's report (dt)
    def dtbeitrJahrgGrp(self, dt, jVon, jBis, grp):
        Q = "SELECT Distinct b.id, b.titel, aus.jahrgangsstufe FROM (((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE dt.typName=\"%s\" AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d AND b.einzel_gruppe=%s"%(dt, jVon, jBis, grp)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions with tutor's report and work report from students in grades jVon to jBis
    def tutbArbJahrg(self, jVon, jBis):
        #Q = "SELECT Distinct b.id, b.titel, aus.jahrgangsstufe FROM (((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE dt.typName=\"Tutorinnenbericht\" AND dt.typName=\"Arbeitsbericht\" AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d"%(jVon, jBis)
        self.dtbeitrJahrg("Tutorinnenbericht", jVon, jBis)
        self.dtbeitrJahrg("Arbeitsbericht", jVon, jBis)


    #Submissions with tutors from students in grades jVon to jBis
    def beitrTut(self, jVon, jBis):
        Q = "SELECT Distinct b.id, b.titel, t.code FROM ((karte_tutor t INNER JOIN karte_beitrag b ON b.tutor_id=t.id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d ORDER BY b.id"%(jVon, jBis)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    #Beitraege mit Tutbericht und Materialgrundlage mgr
    def tutbMgr(self, mgr):
        Q = "SELECT b.id, b.titel, mg.name FROM ((((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=b.id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE dt.typName=\"Tutorinnenbericht\" AND mg.name=\"%s\""%(mgr)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    #Submissions from year wj made from students in grades from jVon to jBis with tutor.
    def wettJahrgTut(self, wj, jVon, jBis):
        Q = "SELECT Distinct b.id, b.titel, t.code FROM (((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON a.id=aus.autorin_id) ON a.beitrag_id=b.id INNER JOIN karte_tutor t ON t.id=b.tutor_id) WHERE aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d AND w.jahr=%d"%(jVon, jBis, wj)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    #Grade of authors (jg) with submission type (ba) and year of competition (wj)
    def jahrgBartWj(self, jg, ba, wj):
        Q = "SELECT Distinct b.id, b.titel FROM ((((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON a.id=aus.autorin_id) ON a.beitrag_id=b.id) INNER JOIN (karte_beitragsart ba INNER JOIN karte_beitrag_typ bba ON bba.beitragsart_id=ba.id) ON bba.beitrag_id=b.id)  WHERE aus.jahrgangsstufe=%d AND ba.name=\"%s\" AND w.jahr=%d"%(jg, ba, wj)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submission type with source material
    def bartMg(self, bart, mg):
        Q = "SELECT b.id, b.titel FROM ((((karte_beitrag b INNER JOIN karte_beitrag_typ bba  ON bba.beitrag_id=b.id) INNER JOIN karte_beitragsart ba ON bba.beitragsart_id=ba.id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=b.id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE ba.name=\"%s\" AND mg.name=\"%s\""%(bart, mg)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    ##################
    #History competition
    ##################

    #Number of submissions in the years v to b
    def anzBeitr(self, v, b):
        Q = "SELECT COUNT(b.id) FROM (karte_beitrag b INNER JOIN karte_beitragwettbewerb wb ON b.id=wb.beitrag_id INNER JOIN karte_wettbewerb w ON wb.wettbewerb_id=w.id) WHERE w.jahr>=%d AND w.jahr<=%d"%(v, b)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    #submissions with awards
    def themaAusz(self):
        Q = "SELECT b.id, b.titel, b.regest FROM ((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON b.id=ea.einreichung_id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) WHERE ea.id>0"
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Submissions with awards and work report
    def auszArb(self):
        Q = "SELECT b.id, b.titel, a.name FROM (((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON b.id=ea.einreichung_id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) INNER JOIN karte_dokument d ON b.id=d.beitrag_id INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) WHERE dt.typName=\"Arbeitsbericht\" ORDER BY b.id"
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor


    ###################
    #3 Quantitative queries
    ###################

    #Amount of single/group submissions
    def countEG(self, grp):
        Q = "SELECT COUNT(b.einzel_gruppe) FROM karte_beitrag b WHERE b.einzel_gruppe=%s"%grp
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Amount of single/group submissions per year
    def countEGJ(self, grp, y):
        Q = "SELECT COUNT(b.einzel_gruppe) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id) INNER JOIN  karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE b.einzel_gruppe=%s AND w.Jahr=%d"%(grp,y)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of submissions with tutor per year
    def tutProJahr(self, year):
        Q = "SELECT COUNT(b.id) FROM (((karte_beitrag b INNER JOIN karte_tutor t ON b.tutor_id=t.id) INNER JOIN karte_beitragwettbewerb bw ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.jahr=%d"%(year)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Amount of submissions for each year
    def countEGW(self, year):
        Q = "SELECT COUNT(b.id) FROM karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id WHERE w.jahr=%d"%(year)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Average scope of each submission per year
    def avgScope(self, year):
        Q = "SELECT AVG(b.umfang) FROM (karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.jahr=%d"%(year)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of submissions by schooltype per year
    def countStYear(self, st, year):
        Q = "SELECT COUNT(Distinct b.id) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN (((karte_autorin a INNER JOIN karte_autorinschule asch ON a.id=asch.autorin_id) INNER JOIN karte_schuleschulart ssa ON ssa.schule_id=asch.schule_id) INNER JOIN karte_schulart sa ON sa.id=ssa.art_id) ON b.id=a.beitrag_id) WHERE sa.name=\"%s\" AND w.jahr=%d"%(st, year)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of place per year
    def countPlaceYear(self, year, oname):
        Q = "SELECT COUNT(o.id) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN karte_ort_beitraege ob ON ob.beitrag_id=b.id INNER JOIN karte_ort o ON o.id=ob.ort_id) WHERE w.jahr=%d AND o.ortbezeichnung=\"%s\""%(year, oname)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of topics per year
    def countTopicYear(self, t, year):
        Q = "SELECT Count(Distinct b.id) FROM (karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.jahr=" + str(year) + " AND (b.titel LIKE \"%" + t + "%\" OR b.regest LIKE \"%" + t + "%\")"
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of persons per year
    def countPersonYear(self, persname, year):
        Q = "SELECT Count(p.id) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN karte_beitrag_persoenlichkeiten bp ON bp.beitrag_id=b.id INNER JOIN karte_persoenlichkeit p ON p.id=bp.persoenlichkeit_id) WHERE p.name=\"%s\" AND w.jahr=%d"%(persname, year)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of submissions that received an award per year
    def countAuszJahr(self, x):
        Q = "SELECT w.jahr, COUNT(a.name) FROM (((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON ea.einreichung_id=b.id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) INNER JOIN (karte_beitragwettbewerb bw INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) ON bw.beitrag_id=b.id) WHERE w.jahr=%d"%(x)
        mycursor.execute(Q)
        self.printCursor(mycursor)
        return mycursor

    #Number of submissions that received an award for every year since 1986
    def countAuszJahrLoop(self):
        i = 1986
        while i <= 2018:
            Q = "SELECT w.jahr, COUNT(a.name)  FROM (((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON ea.einreichung_id=b.id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) INNER JOIN (karte_beitragwettbewerb bw INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) ON bw.beitrag_id=b.id) WHERE w.jahr=%d"%(i)
            mycursor.execute(Q)
            self.printCursor(mycursor)
            i = i+2
