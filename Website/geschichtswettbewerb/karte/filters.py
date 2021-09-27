from .models import *
import django_filters
from django.db.models import Q
from django import forms

class OrtFilter(django_filters.FilterSet):
    """Class for the starting page filter"""
    everything = django_filters.CharFilter(label='everything', method='lookupEverything')

    def lookupEverything(self, queryset, name, value):
        return queryset.filter(Q(titel__icontains=value)
                                |Q(regest__icontains=value)
                                |Q(signatur__icontains=value)
                                |Q(persoenlichkeiten__name__icontains=value)
                                |Q(typ__name__icontains=value)
                                |Q(wettbewerb__thema__icontains=value)
                                |Q(wettbewerb__kurztitel__icontains=value)
                                #|Q(wettbewerb__zusammenfassung__icontains=value)
                                |Q(grundlagen__name__icontains=value)
                                |Q(autorin__schools__name__icontains=value)
                                |Q(autorin__schools__art__name__icontains=value)
                                |Q(auszeichnungeinreichung__auszeichnung__name__icontains=value)
                                |Q(dokument__typ__typName__icontains=value)
                                |Q(ort__histName__name__icontains=value)
                                |Q(ort__histRegion__name__icontains=value)
                                |Q(ort__ortbezeichnung__icontains=value)
                                |Q(institutionen__name__icontains=value)
                                |Q(grundlagen__name__icontains=value)).distinct()

    class Meta:
        """Class to apply the filter on the ortbezeichnung attribute of the Ort model"""
        model = Beitrag

        fields = {
            'ort__ortbezeichnung': ['icontains'],
            'wettbewerb': ['exact'],
            'zeitraumVon': ['gt',],
            'zeitraumBis': ['lt'],
        }

GROUP_CHOICES = {
    ('0', 'Gruppenarbeit'),
    ('1', 'Einzelarbeit'),
}

class BeitragFilter(django_filters.FilterSet):
    """Class for the detail filter"""
    topic = django_filters.CharFilter(label='test', method='lookupTopic')

    einzel_gruppe = django_filters.ChoiceFilter(label='einzel', choices=GROUP_CHOICES, empty_label="Einzel- oder Gruppenarbeit")

    autorin__schools__art = django_filters.ModelMultipleChoiceFilter(label = 'schulart', queryset=Schulart.objects.all())

    dokument__typ = django_filters.ModelMultipleChoiceFilter(label = 'dokumentTypen', queryset=DokumentTyp.objects.all())

    auszeichnungeinreichung__auszeichnung = django_filters.ModelMultipleChoiceFilter(label = 'auszeichnungen', queryset=Auszeichnung.objects.all())

    autorin__autorinschule__schule = django_filters.ModelMultipleChoiceFilter(label = 'schule', queryset=Schule.objects.all())

    jahrgangMin = django_filters.NumberFilter(label='jahrgang', method='lookupGradeGt')
    jahrgangMax = django_filters.NumberFilter(label='jahrgang', method='lookupGradeLt')
    zeitraumVon = django_filters.NumberFilter(label='zeitraum', method='lookupYearFromInterval')
    zeitraumBis = django_filters.NumberFilter(label='zeitraum', method='lookupYearToInterval')

    tutor = django_filters.BooleanFilter(field_name='tutor', method='tutorIsNull')

    def tutorIsNull(self, queryset, name, value):
        return queryset.filter(Q(tutor__isnull=value))

    def lookupTopic(self, queryset, name, value):
        return queryset.filter(Q(titel__icontains=value)|Q(regest__icontains=value))

    def lookupGradeGt(self, queryset, name, value):
        return queryset.filter(Q(beitragwettbewerb__beitrag__jahrgaenge__stufe__gte=value)).distinct()

    def lookupGradeLt(self, queryset, name, value):
        return queryset.filter(Q(beitragwettbewerb__beitrag__jahrgaenge__stufe__lte=value)).distinct()

    def lookupYearFromInterval(self, queryset, name, value):
        return queryset.filter(Q(zeitraumVon__gte=value-15) & Q(zeitraumVon__lte=value + 15)).distinct()

    def lookupYearToInterval(self, queryset, name, value):
        return queryset.filter(Q(zeitraumBis__gte=(value-15)) & Q(zeitraumBis__lte=(value+15))).distinct()

    class Meta:
        model = Beitrag

        fields = {
            'titel': ['icontains'],
            'regest': ['icontains', 'exact'],
            'signatur': ['icontains', 'exact'],
            'persoenlichkeiten': ['exact'],
            'persoenlichkeiten__name': ['icontains'],
            'typ': ['exact'],
            'wettbewerb': ['exact'],
            'ort' : ['exact'],
            'ort__ortbezeichnung' : ['icontains'],
            'institutionen': ['exact'],
            'institutionen__name': ['icontains'],
            'grundlagen': ['exact'],
            'autorin__schools': ['exact'],
        }
