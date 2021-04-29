from django.contrib.gis import admin

from.models import *
# Register your models here.
admin.site.register(Beitrag)
admin.site.register(Auszeichnung)
#admin.site.register(Schulart)
#admin.site.register(Schule)
#admin.site.register(SchuleSchulart)
admin.site.register(Wettbewerb)
admin.site.register(Materialgrundlage)
admin.site.register(DokumentTyp)
admin.site.register(Dokument)
admin.site.register(Institution)
admin.site.register(Tutor)
admin.site.register(Persoenlichkeit)
admin.site.register(Beitragsart)
admin.site.register(BeitragWettbewerb)
admin.site.register(Autorin)
admin.site.register(AutorinSchule)
admin.site.register(AuszeichnungEinreichung)
admin.site.register(HistorischerOrt)
admin.site.register(HistorischeRegion)

@admin.register(Ort)
class OrtAdmin(admin.OSMGeoAdmin):
    list_filter = ('ortbezeichnung', 'location')

class SchuleSchulartInline(admin.TabularInline):
    model = SchuleSchulart
    extra = 1

class SchulAdmin(admin.ModelAdmin):
    inlines = (SchuleSchulartInline,)

class SchulartAdmin(admin.ModelAdmin):
    inlines = (SchuleSchulartInline,)

#admin.site.unregister(Schulart)
#admin.site.unregister(Schule)

admin.site.register(Schule, SchulAdmin)
admin.site.register(Schulart, SchulartAdmin)
