"""This file contains all models for the geschichtswettbewerb database"""

from django.db import models
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models import PointField


class Auszeichnung(models.Model):
    """A class that represents the model for awards, containing a name and an id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Auszeichnungen"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class Schulart(models.Model):
    """A class that represents the model for school types, containing a name and an id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Schularten"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name


class Schule(models.Model):
    """A class that represents the model for schools, containing a name and an id attribute"""
    name = models.CharField(max_length=1024)
    art = models.ManyToManyField(Schulart, through = 'SchuleSchulart', blank=True)

    class Meta:
        verbose_name_plural = "Schulen"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class SchuleSchulart(models.Model):
    """A class that represents the relation between schools and school types containing an attribute for schule and schulart(art)"""
    schule = models.ForeignKey(Schule, on_delete=models.CASCADE)
    art = models.ForeignKey(Schulart, on_delete=models.CASCADE)
    class Meta:
        """Class to set unique constrain on schule and art"""
        unique_together = (('schule', 'art'),)
        verbose_name_plural = "Schulen Schularten"

    def __str__(self):
        """returns the name of the Schule and Schulart model as string"""
        return self.schule.name + ' (' + self.art.name + ')'

class Wettbewerb(models.Model):
    """A class that represents the model for competitions, containing a id, thema,kurztitel, jahr and zusammenfassung attribute"""
    thema = models.TextField()
    kurztitel = models.TextField()
    jahr = models.IntegerField()
    jahrBis = models.IntegerField(null=True)
    zusammenfassung = models.TextField(default = 'Zusammenfassung')

    class Meta:
        verbose_name_plural = "Wettbewerbe"

    def __str__(self):
        """returns the thema and id of the model as string"""
        return self.thema + ' (' + str(self.jahr) + '-' + str(self.jahrBis) + ')'

class Materialgrundlage(models.Model):
    """A class that represents the model for source materials, containing a name and an id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Materialgrundlagen"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class DokumentTyp(models.Model):
    """A class that represents the model for document types, containing a name and an id attribute"""
    typName = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Dokument Type"
        verbose_name_plural = "Dokument Typen"

    def __str__(self):
        """returns the typName and id of the model as string"""
        return self.typName

class Institution(models.Model):
    """A class that represents the model for institutions, containing a name and an id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "institutionen"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class Tutor(models.Model):
    """A class that represents the model for tutors, containing a code, id, first name and surname as attributes"""
    code = models.CharField(max_length=255)
    vorname = models.CharField(max_length=255, null=True)
    nachname = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "Tutorin"
        verbose_name_plural = "Tutorinnen"

    def __str__(self):
        """returns the code and id of the model as string"""
        return self.code

class Persoenlichkeit(models.Model):
    """A class that represents the model for personalities, containing a name, id and gnd as attributes"""
    name = models.CharField(max_length=255)
    gnd = models.CharField(max_length=255, null=True)

    class Meta:
        verbose_name = "Persönlichkeit"
        verbose_name_plural = "Persönlichkeiten"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class Beitragsart(models.Model):
    """A class that represents the model for submission types, containing a name and an id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Beitragsarten"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class Beitrag(models.Model):
    """A class that represents the model for submissions, containing a titel, regest, signatur, einzel_gruppe, umfang, zeitraumVon, zeitraumBis and tutor and an id as attributes"""
    titel = models.CharField(max_length=1024)
    regest = models.TextField()
    signatur = models.CharField(max_length=255)
    einzel_gruppe = models.BooleanField(default=True)
    umfang = models.IntegerField()
    zeitraumVon = models.IntegerField(null=True)
    zeitraumBis = models.IntegerField(null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, null=True)
    grundlagen = models.ManyToManyField(Materialgrundlage, blank=True)
    persoenlichkeiten = models.ManyToManyField(Persoenlichkeit, blank=True)
    institutionen = models.ManyToManyField(Institution, blank=True)
    typ = models.ManyToManyField(Beitragsart, blank=True)
    wettbewerb = models.ManyToManyField(Wettbewerb, through='BeitragWettbewerb', blank=True)

    class Meta:
        verbose_name_plural = "Beiträge"
        ordering = ('signatur',)

    def __str__(self):
        """returns the titel and id of the model as string"""
        return self.titel + '  \n Signatur: ' + self.signatur

class Dokument(models.Model):
    """A class that represents the model for documents, containing a document, submission, document type an id as attributes"""
    dokument = models.FileField(null=True)
    beitrag = models.ForeignKey(Beitrag, on_delete=models.CASCADE, null=True)
    typ = models.ForeignKey(DokumentTyp, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Dokumente"

class BeitragWettbewerb(models.Model):
    """A class that represents the relation between competitions and submissions"""
    beitrag = models.ForeignKey(Beitrag, on_delete=models.CASCADE, null=True, unique=True)
    wettbewerb = models.ForeignKey(Wettbewerb, on_delete=models.CASCADE)
    class Meta:
        """Class to set unique constraint on beitrag and wettbewerb"""
        unique_together = (('beitrag', 'wettbewerb'),)
        verbose_name_plural = "Beiträge Wettbewerbe"


class Autorin(models.Model):
    """A class that represents the model for authors, containing a first name, surname, submission and id attribute"""
    vorname = models.CharField(max_length=255, null=True)
    nachname = models.CharField(max_length=255, null=True)
    schule = models.ManyToManyField(SchuleSchulart, through='AutorinSchule', blank=True)
    beitrag = models.ForeignKey(Beitrag, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Autorinnen"

    def __str__(self):
        """returns the vorname and nachname of the model as string"""
        return self.vorname + ' ' + self.nachname

class AutorinSchule(models.Model):
    """A class that represents the relation between authors and schools containing a grade attribute"""
    autorin = models.ForeignKey(Autorin, on_delete=models.CASCADE)
    schule = models.ForeignKey(SchuleSchulart, on_delete=models.CASCADE)
    jahrgangsstufe = models.IntegerField(null=True)
    class Meta:
        """Class to set unique constraint on schule and autorin"""
        unique_together = (('schule', 'autorin'),)
        verbose_name_plural = "Autorinnen Schulen"

#    def __str__(self):
#        return str(self.jahrgangsstufe)

class AuszeichnungEinreichung(models.Model):
    """A class that represents the relation between submissions and awards"""
    einreichung = models.ForeignKey(Beitrag, on_delete=models.CASCADE, null=True)
    auszeichnung = models.ForeignKey(Auszeichnung, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name_plural = "Auszeichnungen Einreichungen"

class HistorischerOrt(models.Model):
    """A class that represents the model for historical places, containing a name and id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Historischer Ort"
        verbose_name_plural = "Historische Orte"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class HistorischeRegion(models.Model):
    """A class that represents the model for historical regions, containing a name and id attribute"""
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Historische Region"
        verbose_name_plural = "Historische Regionen"

    def __str__(self):
        """returns the name and id of the model as string"""
        return self.name

class Ort(models.Model):
    """A class that represents the model for places, containing a name, location and id attribute"""
    ortbezeichnung = models.CharField(max_length=255)
    location = PointField(geography=True, default=Point(0.0, 0.0))
    beitraege = models.ManyToManyField(Beitrag, blank=True)
    histName = models.ManyToManyField(HistorischerOrt, blank=True)
    histRegion = models.ManyToManyField(HistorischeRegion, blank=True)

    class Meta:
        verbose_name_plural = "Orte"

    def __str__(self):
        """returns the ortbezeichnung and id of the model as string"""
        return self.ortbezeichnung
