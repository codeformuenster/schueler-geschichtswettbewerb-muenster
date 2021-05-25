from django.urls import path
from .views import PlaceMapView, PlaceListView, SubmissionDetailView
from karte import views
from django.views.generic import RedirectView

app_name = 'karte'

urlpatterns = [
    path('', views.index, name='index'),
    path('karte/', PlaceMapView.as_view(), name = 'karte'),
    path('orte/', views.PlaceListView.as_view(), name='orte'),
    path('beitraege/', views.SubmissionFilterView.as_view(), name='beitraege'),
    path('karte/<int:pk>', views.PlaceDetailView.as_view(), name='ort-detail'),
    path('orte/<int:pk>', views.PlaceDetailView.as_view(), name='ort-detail'),
    path('beitraege/<int:pk>', views.SubmissionDetailView.as_view(), name='submission-detail'),

]
