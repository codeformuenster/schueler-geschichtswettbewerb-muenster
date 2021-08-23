from .models import *
import django_filters
from django.db.models import Q

class OrtFilter(django_filters.FilterSet):
    """Class to filter place data"""
    everything = django_filters.CharFilter(label='everything', method='lookupEverything')

    def lookupEverything(self, queryset, name, value):
        return queryset.filter(Q(titel__icontains=value)
                                |Q(regest__icontains=value)
                                |Q(signatur__icontains=value)
                                |Q(persoenlichkeiten__name__icontains=value)
                                |Q(typ__icontains=value)
                                |Q(wettbewerb__icontains=value)
                                |Q(ort__ortbezeichnung__icontains=value)
                                |Q(institutionen__name__icontains=value)
                                |Q(grundlagen__name__icontains=value))

    class Meta:
        """Class to apply the filter on the ortbezeichnung attribute of the Ort model"""
        model = Beitrag

        fields = {
            'ort__ortbezeichnung': ['icontains'],
            'wettbewerb': ['exact'],
            'zeitraumVon': ['gt',],
            'zeitraumBis': ['lt'],
        }

class SimpleFilter(django_filters.FilterSet):
    """Class for the simple filter in the front page"""
    everything = django_filters.CharFilter(label='everything', method='lookupEverything')

    def lookupEverything(self, queryset, name, value):
        return queryset.filter(Q(titel__icontains=value)
                                |Q(regest__icontains=value)
                                |Q(signatur__icontains=value)
                                |Q(persoenlichkeiten__name__icontains=value)
                                |Q(typ__icontains=value)
                                |Q(wettbewerb__icontains=value)
                                |Q(ort__ortbezeichnung__icontains=value)
                                |Q(institutionen__name__icontains=value)
                                |Q(grundlagen__name__icontains=value))
    class Meta:
        model=Beitrag
        fields = {}
GROUP_CHOICES = {
    ('0', 'Gruppenarbeit'),
    ('1', 'Einzelarbeit'),
}

class BeitragFilter(django_filters.FilterSet):
    """Class to filter submissions by persons"""
    topic = django_filters.CharFilter(label='test', method='lookupTopic')

    einzel_gruppe = django_filters.ChoiceFilter(label='einzel', choices=GROUP_CHOICES)

    autorin__autorinschule__schule__art = django_filters.ModelMultipleChoiceFilter(label = 'schulart', queryset=Schulart.objects.all())

    dokument__typ = django_filters.ModelMultipleChoiceFilter(label = 'dokumentTypen', queryset=DokumentTyp.objects.all())

    auszeichnungeinreichung__auszeichnung = django_filters.ModelMultipleChoiceFilter(label = 'auszeichnungen', queryset=Auszeichnung.objects.all())


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

        fields = {
            'titel': ['icontains'],
            'regest': ['icontains', 'exact'],
            'signatur': ['icontains', 'exact'],
            'persoenlichkeiten': ['exact'],
            'persoenlichkeiten__name': ['icontains'],
            'zeitraumVon': ['exact', 'gt', 'lt',],
            'zeitraumBis': ['exact', 'gt', 'lt'],
            'typ': ['exact'],
            'wettbewerb': ['exact'],
            'wettbewerb__jahr' : ['exact', 'gt', 'lt'],
            'ort' : ['exact'],
            'ort__ortbezeichnung' : ['icontains'],
            'institutionen': ['exact'],
            'institutionen__name': ['icontains'],
            'grundlagen': ['exact'],
            'tutor': ['exact', 'isnull'],
        }
