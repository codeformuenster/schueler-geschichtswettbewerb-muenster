from .models import *
import django_filters
from django.db.models import Q

class OrtFilter(django_filters.FilterSet):
    """Class to filter place data"""
    class Meta:
        """Class to apply the filter on the ortbezeichnung attribute of the Ort model"""
        model = Ort
        fields = {
            'ortbezeichnung': ['icontains'],
        }

GROUP_CHOICES = {
    ('0', 'Gruppenarbeit'),
    ('1', 'Einzelarbeit'),
    ('', 'Alle')
}
class PersonFilter(django_filters.FilterSet):
    """Class to filter submissions by persons"""
    topic = django_filters.CharFilter(label='test', method='lookupTopic')

    einzel_gruppe = django_filters.ChoiceFilter(label='einzel', choices=GROUP_CHOICES)

    autorin__autorinschule__schule__art = django_filters.ModelMultipleChoiceFilter(label = 'schulart', queryset=Schulart.objects.all())

    dokument__typ = django_filters.ModelMultipleChoiceFilter(label = 'dokumentTypen', queryset=DokumentTyp.objects.all())

    auszeichnungeinreichung__auszeichnung = django_filters.ModelMultipleChoiceFilter(label = 'auszeichnungen', queryset=Auszeichnung.objects.all())

    #autorin__autorinschule__jahrgangsstufe = django_filters.NumberFilter(label='jahrgang', method='lookupGrade')
    #autorin__autorinschule__jahrgangsstufe__gt = django_filters.NumberFilter(label='jahrgangMin')
    #autorin__autorinschule__jahrgangsstufe__lt = django_filters.NumberFilter(label='jahrgangMax')
    jahrgang = django_filters.NumberFilter(label='jahrgang', method='lookupGradeExact')
    jahrgangMin = django_filters.NumberFilter(label='jahrgang', method='lookupGradeGt')
    jahrgangMax = django_filters.NumberFilter(label='jahrgang', method='lookupGradeLt')


    def lookupTopic(self, queryset, name, value):
        return queryset.filter(Q(titel__icontains=value)|Q(regest__icontains=value))

    def lookupGradeExact(self, queryset, name, value):
        return queryset.filter(Q(beitragwettbewerb__beitrag__autorin__autorinschule__jahrgangsstufe=value)).distinct()

    def lookupGradeGt(self, queryset, name, value):
        return queryset.filter(Q(beitragwettbewerb__beitrag__autorin__autorinschule__jahrgangsstufe__gt=value)).distinct()

    def lookupGradeLt(self, queryset, name, value):
        return queryset.filter(Q(beitragwettbewerb__beitrag__autorin__autorinschule__jahrgangsstufe__lt=value)).distinct()
    class Meta:
        model = Beitrag

        #fields = ['titel', 'persoenlichkeiten']
        fields = {
            'titel': ['icontains'],
            'regest': ['icontains', 'exact'],
            'signatur': ['icontains', 'exact'],
            'persoenlichkeiten': ['exact'],
            'persoenlichkeiten__name': ['icontains'],
            #'einzel_gruppe': ['exact'],
            'zeitraumVon': ['exact', 'gt', 'lt',],
            'zeitraumBis': ['exact', 'gt', 'lt'],
            'typ': ['exact'],
            'wettbewerb': ['exact'],
            'wettbewerb__jahr' : ['exact', 'gt', 'lt'],
            'ort' : ['exact'],
            'ort__ortbezeichnung' : ['icontains'],
            #'dokument__typ' : ['exact'],
            'institutionen': ['exact'],
            'institutionen__name': ['icontains'],
            'grundlagen': ['exact'],
            #'autorin__autorinschule__schule__art' : ['exact'],
            #'autorin__autorinschule__jahrgangsstufe': ['exact', 'gt', 'lt',],
            #'auszeichnungeinreichung__auszeichnung': ['exact'],
        }
