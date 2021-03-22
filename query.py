"""The file contains a class to execute queries on the geschichtswettbewerb database"""

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="geschichtswettbewerb",
    auth_plugin='caching_sha2_password'
)



class Query:
    """A class that contains methods to execute all required queries and prints them to the command line.
        The methods provide the functionallity to execute all queries defined in 2020_11_11_Vorschlage_Suchanfragen.pdf
    """

    def __init__(self):
        """Constructs the cursor attribute for the query object."""
        self.mycursor = db.cursor()

    def printCursor(self, cursor):
        """Print a cursor object."""
        for x in cursor:
            print(x)

    def queryCount(self, cursor):
        """Get the count of any query"""
        print(cursor.rowcount)


    def autorinBeitrag(self):
        """Get all authors with their respective submissions."""
        Q = "SELECT b.id, b.signatur, a.vorname, a.nachname, a.id FROM karte_beitrag b INNER JOIN karte_autorin a ON a.beitrag_id=b.id"
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    ####################################
    #1 Content
    ####################################

    def beitrFromTo(self, x, y):
        """Query for submissions that write about the time period from x to y"""
        Q = "SELECT b.id, b.titel FROM karte_beitrag b WHERE zeitraumVon >= %d AND zeitraumBis <= %d" %(x, y)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def beitragPlace(self, p, x = 0, y = 2020):
        """Select Beitrag to a place p dealing with the years x to y"""
        Q = "SELECT o.ortbezeichnung, o.id, b.id, b.titel FROM ((karte_ort_beitraege bo INNER JOIN karte_ort o ON o.id=bo.ort_id) INNER JOIN karte_beitrag b ON bo.beitrag_id=b.id) WHERE ortbezeichnung=\"%s\" AND zeitraumVon>=%d AND zeitraumBis<=%d" %(p, x, y)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def beitragPerson(self, pers):
        """Submissions that are about person pers."""
        Q = "SELECT b.id, b.titel, p.name, p.id FROM ((karte_beitrag_persoenlichkeiten bp INNER JOIN karte_persoenlichkeit p ON bp.persoenlichkeit_id=p.id) INNER JOIN karte_beitrag b ON b.id=bp.beitrag_id) WHERE p.name=\"%s\""%(pers)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def ortPers(self, place, pers):
        """Returns all submissions about a given place (place) and person (pers)."""
        Q = "SELECT b.id, b.titel, p.name, p.id, o.ortbezeichnung, o.id FROM (((karte_ort_beitraege bo INNER JOIN karte_ort o ON bo.ort_id=o.id) INNER JOIN karte_beitrag b ON b.id=bo.beitrag_id) INNER JOIN (karte_beitrag_persoenlichkeiten bp INNER JOIN karte_persoenlichkeit p ON bp.persoenlichkeit_id=p.id) ON bp.beitrag_id=bo.beitrag_id) WHERE o.ortbezeichnung=\"%s\" AND p.name=\"%s\""%(place, pers)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def beitrWett(self, w):
        """Submissions handed in at competition with title w."""
        Q = "SELECT b.id, b.titel, w.id, w.thema FROM ((karte_beitragwettbewerb bw INNER JOIN karte_beitrag b ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.thema=\"%s\"" %(w)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    """Submissions handed in to competition w dealing with place o."""
    def wettOrt(self, w, o):
        Q = "SELECT b.id, b.titel, w.id, w.thema, o.ortbezeichnung, bo.ort_id FROM ((((karte_ort_beitraege bo INNER JOIN karte_ort o ON o.id=bo.ort_id) INNER JOIN karte_beitrag b ON bo.beitrag_id=b.id) INNER JOIN karte_beitragwettbewerb bw ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.thema=\"%s\" AND o.ortbezeichnung=\"%s\""%(w, o)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def tutJahr(self, x):
        """Submissions with tutors of competition year x"""
        Q = "SELECT b.id, b.titel, w.thema, w.id FROM ((karte_beitragwettbewerb bw INNER JOIN karte_beitrag b ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE b.tutor_id>0 AND w.jahr=%d"%(x)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def tutJahrgang(self, js, jahr):
        """Submissions from authors of grade js and submission year jahr."""
        Q = "SELECT b.id, b.titel FROM ((((karte_beitrag b INNER JOIN karte_beitragwettbewerb wb ON b.id=wb.beitrag_id)INNER JOIN karte_wettbewerb w ON w.id=wb.wettbewerb_id)) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE aus.jahrgangsstufe=%d AND w.jahr=%d"%(js, jahr)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def mGrundlage(self, x):
        """Submissions with source material x."""
        Q = "SELECT b.id, b.titel, mg.name, mg.id FROM ((karte_beitrag b INNER JOIN karte_beitrag_grundlagen bg ON b.id=bg.beitrag_id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE mg.name=\"%s\""%(x)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def mgJahr(self, bta, jahr):
        """Submissions of a certain type bta submitted at competition year jahr."""
        Q = "SELECT b.id, b.titel, w.jahr, w.id FROM (((karte_beitrag b INNER JOIN karte_beitrag_typ bba ON b.id=bba.beitrag_id) INNER JOIN karte_beitragsart ba ON ba.id=bba.beitragsart_id) INNER JOIN (karte_beitragwettbewerb bw INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) ON bw.beitrag_id=b.id) WHERE ba.name=%s AND w.jahr=%d"%(bta, jahr)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def baBgr(self, bta, mgr):
        """Submission with given type bta and source material mgr"""
        Q = "SELECT ba.name, mg.name, b.titel, b.id FROM (((((karte_beitrag b INNER JOIN karte_beitrag_typ bba ON b.id=bba.beitrag_id) INNER JOIN karte_beitragsart ba ON ba.id=bba.beitragsart_id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=b.id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id)) WHERE ba.name=\"%s\" AND mg.name=\"%s\""%(bta,mgr)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def bAusz(self):
        """Submissions that received awards."""
        Q = "SELECT b.id, b.titel, a.name FROM ((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON b.id=ea.einreichung_id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) WHERE ea.id>0"
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    def ortMG(self, o, mgr):
        """Submissions about a place o using source material mgr."""
        Q = "SELECT b.id, b.titel, o.ortbezeichnung, mg.name FROM ((((karte_beitrag b INNER JOIN karte_ort_beitraege bo ON b.id=bo.beitrag_id) INNER JOIN karte_ort o ON o.id=bo.ort_id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=bo.beitrag_id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE o.ortbezeichnung=\"%s\" AND mg.name=\"%s\""%(o,mgr)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    def beitrThema(self, t):
        """Submissions that are about a certain topic t. The topic is searched within the title and regest of the submissions."""
        Q = "SELECT b.id, b.titel FROM karte_beitrag b WHERE b.titel LIKE \"%" + t + "%\" OR b.regest LIKE \"%" + t + "%\""
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    ###################
    #2 Working methods
    ###################

    def grpJahrg(self, jVon, jBis, grp):
        """Submissions from authors in grade jVon to jBis woking allone (grp="True") or in a group (grp="False")"""
        Q = "SELECT b.id, b.titel, aus.jahrgangsstufe, b.einzel_gruppe FROM ((karte_beitrag b INNER JOIN karte_autorin a ON a.beitrag_id=b.id) INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) WHERE b.einzel_gruppe=%d AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d"%(grp, jVon, jBis)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def dtbeitrJahrg(self, dt, jVon, jBis):
        """Submissions from students of grade jVon to jBis containing documents of type dt"""
        Q = "SELECT Distinct b.id, b.titel, aus.jahrgangsstufe FROM (((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE dt.typName=\"%s\" AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d"%(dt, jVon, jBis)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def dtbeitrJahrgGrp(self, dt, jVon, jBis, grp):
        """Submissions from students in grades from jVon to jBis who worked allown or in a group (grp) containing a work report or tutor's report (dt)"""
        Q = "SELECT Distinct b.id, b.titel, aus.jahrgangsstufe FROM (((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE dt.typName=\"%s\" AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d AND b.einzel_gruppe=%s"%(dt, jVon, jBis, grp)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def tutbArbJahrg(self, jVon, jBis):
        """Submissions with tutor's report and submissions with work report from students in grades jVon to jBis"""
        #Q = "SELECT Distinct b.id, b.titel, aus.jahrgangsstufe FROM (((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE dt.typName=\"Tutorinnenbericht\" AND dt.typName=\"Arbeitsbericht\" AND aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d"%(jVon, jBis)
        self.dtbeitrJahrg("Tutorinnenbericht", jVon, jBis)
        self.dtbeitrJahrg("Arbeitsbericht", jVon, jBis)


    def beitrTut(self, jVon, jBis):
        """Submissions with tutors from students in grades jVon to jBis"""
        Q = "SELECT Distinct b.id, b.titel, t.code FROM ((karte_tutor t INNER JOIN karte_beitrag b ON b.tutor_id=t.id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON aus.autorin_id=a.id) ON a.beitrag_id=b.id) WHERE aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d ORDER BY b.id"%(jVon, jBis)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    def tutbMgr(self, mgr):
        """Submissions with tutor's report and source material mgr"""
        Q = "SELECT b.id, b.titel, mg.name FROM ((((karte_beitrag b INNER JOIN karte_dokument d ON b.id=d.beitrag_id) INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=b.id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE dt.typName=\"Tutorinnenbericht\" AND mg.name=\"%s\""%(mgr)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    def wettJahrgTut(self, wj, jVon, jBis):
        """Submissions from year wj made from students in grades from jVon to jBis with tutor."""
        Q = "SELECT Distinct b.id, b.titel, t.code FROM (((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON a.id=aus.autorin_id) ON a.beitrag_id=b.id INNER JOIN karte_tutor t ON t.id=b.tutor_id) WHERE aus.jahrgangsstufe>=%d AND aus.jahrgangsstufe<=%d AND w.jahr=%d"%(jVon, jBis, wj)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    def jahrgBartWj(self, jg, ba, wj):
        """Grade of authors (jg) with submission type (ba) and year of competition (wj)"""
        Q = "SELECT Distinct b.id, b.titel FROM ((((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN (karte_autorin a INNER JOIN karte_autorinschule aus ON a.id=aus.autorin_id) ON a.beitrag_id=b.id) INNER JOIN (karte_beitragsart ba INNER JOIN karte_beitrag_typ bba ON bba.beitragsart_id=ba.id) ON bba.beitrag_id=b.id)  WHERE aus.jahrgangsstufe=%d AND ba.name=\"%s\" AND w.jahr=%d"%(jg, ba, wj)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def bartMg(self, bart, mg):
        """Submission type with source material"""
        Q = "SELECT b.id, b.titel FROM ((((karte_beitrag b INNER JOIN karte_beitrag_typ bba  ON bba.beitrag_id=b.id) INNER JOIN karte_beitragsart ba ON bba.beitragsart_id=ba.id) INNER JOIN karte_beitrag_grundlagen bg ON bg.beitrag_id=b.id) INNER JOIN karte_materialgrundlage mg ON mg.id=bg.materialgrundlage_id) WHERE ba.name=\"%s\" AND mg.name=\"%s\""%(bart, mg)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    ##################
    #History competition
    ##################

    def anzBeitr(self, v, b):
        """Number of submissions in the years v to b"""
        Q = "SELECT COUNT(b.id) FROM (karte_beitrag b INNER JOIN karte_beitragwettbewerb wb ON b.id=wb.beitrag_id INNER JOIN karte_wettbewerb w ON wb.wettbewerb_id=w.id) WHERE w.jahr>=%d AND w.jahr<=%d"%(v, b)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    def themaAusz(self):
        """submissions with awards"""
        Q = "SELECT b.id, b.titel, b.regest FROM ((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON b.id=ea.einreichung_id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) WHERE ea.id>0"
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def auszArb(self):
        """Submissions with awards and work report"""
        Q = "SELECT b.id, b.titel, a.name FROM (((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON b.id=ea.einreichung_id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) INNER JOIN karte_dokument d ON b.id=d.beitrag_id INNER JOIN karte_dokumenttyp dt ON dt.id=d.typ_id) WHERE dt.typName=\"Arbeitsbericht\" ORDER BY b.id"
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor


    ###################
    #3 Quantitative queries
    ###################

    def countEG(self, sng):
        """Amount of single(sng=True) or group(sng=False) submissions"""
        Q = "SELECT COUNT(b.einzel_gruppe) FROM karte_beitrag b WHERE b.einzel_gruppe=%s"%sng
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countEGJ(self, grp, year):
        """Amount of single/group submissions per year"""
        Q = "SELECT COUNT(b.einzel_gruppe) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id) INNER JOIN  karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE b.einzel_gruppe=%s AND w.Jahr=%d"%(grp, year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def tutProJahr(self, year):
        """Number of submissions with tutor per year"""
        Q = "SELECT COUNT(b.id) FROM (((karte_beitrag b INNER JOIN karte_tutor t ON b.tutor_id=t.id) INNER JOIN karte_beitragwettbewerb bw ON bw.beitrag_id=b.id) INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.jahr=%d"%(year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countEGW(self, year):
        """Amount of submissions for a year"""
        Q = "SELECT COUNT(b.id) FROM karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id WHERE w.jahr=%d"%(year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def avgScope(self, year):
        """Average scope of each submission per year"""
        Q = "SELECT AVG(b.umfang) FROM (karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.jahr=%d"%(year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countStYear(self, st, year):
        """Number of submissions by schooltype per year"""
        Q = "SELECT COUNT(Distinct b.id) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN (((karte_autorin a INNER JOIN karte_autorinschule asch ON a.id=asch.autorin_id) INNER JOIN karte_schuleschulart ssa ON ssa.schule_id=asch.schule_id) INNER JOIN karte_schulart sa ON sa.id=ssa.art_id) ON b.id=a.beitrag_id) WHERE sa.name=\"%s\" AND w.jahr=%d"%(st, year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countPlaceYear(self, year, oname):
        """Number of place oname per year"""
        Q = "SELECT COUNT(o.id) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN karte_ort_beitraege ob ON ob.beitrag_id=b.id INNER JOIN karte_ort o ON o.id=ob.ort_id) WHERE w.jahr=%d AND o.ortbezeichnung=\"%s\""%(year, oname)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countTopicYear(self, tutor, year):
        """Number of topics per year"""
        Q = "SELECT Count(Distinct b.id) FROM (karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) WHERE w.jahr=" + str(year) + " AND (b.titel LIKE \"%" + tutor + "%\" OR b.regest LIKE \"%" + tutor + "%\")"
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countPersonYear(self, persname, year):
        """Number of persons per year"""
        Q = "SELECT Count(p.id) FROM ((karte_beitrag b INNER JOIN karte_beitragwettbewerb bw ON b.id=bw.beitrag_id INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) INNER JOIN karte_beitrag_persoenlichkeiten bp ON bp.beitrag_id=b.id INNER JOIN karte_persoenlichkeit p ON p.id=bp.persoenlichkeit_id) WHERE p.name=\"%s\" AND w.jahr=%d"%(persname, year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countAuszJahr(self, year):
        """Number of submissions that received an award per year"""
        Q = "SELECT w.jahr, COUNT(a.name) FROM (((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON ea.einreichung_id=b.id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) INNER JOIN (karte_beitragwettbewerb bw INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) ON bw.beitrag_id=b.id) WHERE w.jahr=%d"%(year)
        self.mycursor.execute(Q)
        self.printCursor(self.mycursor)
        return self.mycursor

    def countAuszJahrLoop(self):
        """Number of submissions that received an award for every year since 1986"""
        i = 1986
        while i <= 2018:
            Q = "SELECT w.jahr, COUNT(a.name)  FROM (((karte_beitrag b INNER JOIN karte_auszeichnungeinreichung ea ON ea.einreichung_id=b.id) INNER JOIN karte_auszeichnung a ON a.id=ea.auszeichnung_id) INNER JOIN (karte_beitragwettbewerb bw INNER JOIN karte_wettbewerb w ON w.id=bw.wettbewerb_id) ON bw.beitrag_id=b.id) WHERE w.jahr=%d"%(i)
            self.mycursor.execute(Q)
            self.printCursor(self.mycursor)
            i = i+2
