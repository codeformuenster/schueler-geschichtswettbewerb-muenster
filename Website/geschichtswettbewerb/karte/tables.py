import django_tables2 as tables
from .models import *

class placeTable(tables.Table):
    class Meta:
        model=Ort
        template_name = "django_tables2/bootstrap.html"
        fields = ("ortbezeichnung", )
