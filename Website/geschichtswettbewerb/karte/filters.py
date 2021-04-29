from .models import *
import django_filters

class OrtFilter(django_filters.FilterSet):
    """Class to filter place data"""
    class Meta:
        """Class to apply the filter on the ortbezeichnung attribute of the Ort model"""
        model = Ort
        fields = {
            'ortbezeichnung': ['icontains'],
        }

class PersonFilter(django_filters.FilterSet):
    """Class to filter submissions by persons"""
    #titel = django_filters.CharFilter(lookup_expr='icontains')

        #persoenlichkeiten = django_filters.ModelMultipleChoiceFilter(queryset=Persoenlichkeit.objects.all())
    class Meta:
        model = Beitrag
        #fields = ['titel', 'persoenlichkeiten']
        fields = {
            'titel': ['icontains'],
            'regest': ['icontains', 'exact'],
            'signatur': ['icontains', 'exact'],
            'persoenlichkeiten': ['exact'],
            'persoenlichkeiten__name': ['icontains'],
            'einzel_gruppe': ['exact'],
            'zeitraumVon': ['exact', 'gt', 'lt',],
            'zeitraumBis': ['exact', 'gt', 'lt'],
            'typ': ['exact'],
            'wettbewerb': ['exact'],
            'wettbewerb__jahr' : ['exact', 'gt', 'lt'],
            'ort' : ['exact'],
            'ort__ortbezeichnung' : ['icontains'],
            'dokument__typ' : ['exact'],
            'institutionen': ['exact'],
            'institutionen__name': ['icontains'],
            'grundlagen': ['exact'],
            'autorin__autorinschule__jahrgangsstufe': ['exact', 'gt', 'lt',],
            'auszeichnungeinreichung__auszeichnung': ['exact'],
        }
#
"""      <ul class="sidebar-nav">
        <li><a href="{% url 'karte:karte' %}">Startseite</a></li>
        <li><a href="{% url 'karte:beitraege' %}">Filter</a></li>
      </ul>
"""
