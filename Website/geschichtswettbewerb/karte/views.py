"""This file contains all views for the website prototype"""

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from django.core.serializers import serialize
from .models import Ort, Beitrag, Persoenlichkeit
from .filters import *
import json

class PlaceMapView(generic.ListView):
    """View for the map with all place entries using the Ort model and map.html template"""
    model = Beitrag
    model2 = Persoenlichkeit
    template_name = 'index.html'
    paginate_by=50
    def get_context_data(self, **kwargs):
        """returns the data for all place markers in a geojson file and a variable to check if the form was submitted"""
        context = super().get_context_data(**kwargs)
        context['markers'] = json.loads(serialize('geojson', Ort.objects.all()))
        submitted = 'submitted' in self.request.GET
        data = self.request.GET if submitted else None
        context['filter'] = OrtFilter(data, queryset=self.get_queryset())
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
    """View for the detail filter of submissions"""
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
    """View for a single submission"""
    model = Beitrag
    template_name = 'submission_detail.html'

    def get_context_data(self, **kwargs):
        """returns all submission data"""
        context = super().get_context_data(**kwargs)
        return context

class CompetitionListView(generic.ListView):
    """View for the competition overview"""
    model = Wettbewerb
    template_name = 'competition_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CompetitionDetailView(generic.DetailView):
    """View for a single competition"""
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
    """View for the impressum"""
    template_name = 'impressum.html'
    model = Beitrag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
