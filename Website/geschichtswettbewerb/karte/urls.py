from django.urls import path
from karte import views
from django.views.generic import RedirectView

app_name = 'karte'

urlpatterns = [
    path('', views.PlaceMapView.as_view(), name='karte'),
    path('beitraege/', views.SubmissionFilterView.as_view(), name='beitraege'),
    path('<int:pk>', views.PlaceDetailView.as_view(), name='ort-detail'),
    path('beitraege/<int:pk>', views.SubmissionDetailView.as_view(), name='submission-detail'),
    path('wettbewerbe',  views.CompetitionListView.as_view(), name='wettbewerbe'),
    path('wettbewerbe/<int:pk>',  views.CompetitionDetailView.as_view(), name='wettbewerb-detail'),
    path('impressum/', views.ImpressumView.as_view(), name='impressum'),
]
