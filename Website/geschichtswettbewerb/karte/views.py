"""This file contains all views for the website prototype"""

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.core.serializers import serialize
from .models import Ort, Beitrag, Persoenlichkeit
from .filters import *
from .tables import *
import json

def index(request):
    """Function that creates the start view"""
    num_places = Ort.objects.all().count()
    num_submissions = Beitrag.objects.all().count()
    context = {
        'num_places' : num_places,
        'num_submissions' : num_submissions,
    }
    return render(request, 'index.html', context = context)


class StartView(generic.ListView):
    model = Beitrag
    #template_name = 'index.html'
    def get_context_data(self, **kwargs):
        """returns the data for the starting page"""
        context = super().get_context_data(**kwargs)
        submitted = 'submitted' in self.request.GET
        data = self.request.GET if submitted else None
        #context['filter'] = SimpleFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = SimpleFilter(data, queryset=self.get_queryset())

        return context


class PlaceMapView(generic.ListView):
    """View for the map with all place entries using the Ort model and map.html template"""
    model = Beitrag
    model2 = Persoenlichkeit
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        """returns the data for all place markers in a geojson file"""
        context = super().get_context_data(**kwargs)
        context['markers'] = json.loads(serialize('geojson', Ort.objects.all()))

        submitted = 'submitted' in self.request.GET
        data = self.request.GET if submitted else None

        #context['filter'] = OrtFilter(self.request.GET, queryset=self.get_queryset())
        context['filter'] = OrtFilter(data, queryset=self.get_queryset())

        #context['schulen'] = SchuleSchulart.objects.filter(Q(schule__autorin_set__beitrag=self.get_queryset())).distinct()


        return context

class PlaceListView(generic.ListView):
    """View for the list of all places using the Ort model and the place_list.html template"""
    model = Ort
    table_class = placeTable
    template_name = 'place_list.html'

    def get_context_data(self, **kwargs):
        """returns the place data that is to be filtered in the view"""
        context = super().get_context_data(**kwargs)
        context['filter'] = OrtFilter(self.request.GET, queryset=self.get_queryset())
        return context

class PlaceDetailView(generic.DetailView):
    """View for places with their location and submissions"""
    model = Ort
    template_name = 'place_detail.html'
    def get_context_data(self, **kwargs):
        """returns the place data as geojson"""
        context = super().get_context_data(**kwargs)
        context['markers'] = json.loads(serialize('geojson', Ort.objects.all()))
        return context


class SubmissionFilterView(generic.ListView):
    model = Beitrag
    template_name = 'beitrag_filter.html'
    def get_context_data(self, **kwargs):
        """returns the place data that is to be filtered in the view"""
        context = super().get_context_data(**kwargs)

        submitted = 'submitted' in self.request.GET
        data = self.request.GET if submitted else None

        context['filter'] = BeitragFilter(data, queryset=self.get_queryset())
        context['markers'] = json.loads(serialize('geojson', Ort.objects.all()))
        return context

class SubmissionDetailView(generic.DetailView):
    model = Beitrag
    template_name = 'submission_detail.html'

    def get_context_data(self, **kwargs):
        """returns all submission data"""
        context = super().get_context_data(**kwargs)
        return context

class CompetitionListView(generic.ListView):
    model = Wettbewerb
    template_name = 'competition_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CompetitionDetailView(generic.DetailView):
    model = Wettbewerb
    template_name = 'competition_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        placeQuerySet = Ort.objects.filter(Q(beitraege__wettbewerb=self.get_object()))
        context['markers'] = json.loads(serialize('geojson', list(placeQuerySet)))
        context['autorinnen'] = Autorin.objects.filter(Q(beitrag__wettbewerb=self.get_object()))
        context['awards'] = AuszeichnungEinreichung.objects.filter(Q(einreichung__wettbewerb=self.get_object()))
        return context

class ImpressumView(generic.ListView):
    template_name = 'impressum.html'
    model = Beitrag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
