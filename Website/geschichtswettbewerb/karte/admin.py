from django.contrib.gis import admin
from django.contrib.admin.models import LogEntry

from.models import *
admin.site.register(Auszeichnung)
admin.site.register(Materialgrundlage)
admin.site.register(DokumentTyp)
admin.site.register(Institution)
admin.site.register(Tutor)
admin.site.register(Persoenlichkeit)
admin.site.register(Beitragsart)
admin.site.register(Autorin)
admin.site.register(AuszeichnungEinreichung)
admin.site.register(HistorischerOrt)
admin.site.register(HistorischeRegion)

@admin.register(Ort)
class OrtAdmin(admin.OSMGeoAdmin):
    """class to create the 'Ort' admin page"""
    list_filter = ('ortbezeichnung', 'location')

class SchuleSchulartInline(admin.TabularInline):
    """class for the SchuleSchulart inline"""
    model = SchuleSchulart
    extra = 1

class DokumentInline(admin.TabularInline):
    """class for the Dokument inline"""
    model = Dokument
    extra = 1

class SchulAdmin(admin.ModelAdmin):
    """class for the Schule admin page"""
    inlines = (SchuleSchulartInline,)

class SchulartAdmin(admin.ModelAdmin):
    """class for the Schulart admin page"""
    inlines = (SchuleSchulartInline,)

class BeitragWettbewerbInline(admin.TabularInline):
    """class for the BeitragWettbewerb inline"""
    model = BeitragWettbewerb
    extra = 1

class BeitragJahrgangInline(admin.TabularInline):
    """class for the Jahrgang inline"""
    model =  Jahrgangsstufe
    extra = 1

class BeitragAdmin(admin.ModelAdmin):
    """class for the Beitrag admin page"""
    inlines = (BeitragWettbewerbInline, DokumentInline)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """class to log admin activity"""
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'action_flag',
    ]
    def has_add_permission(self, request):
        return False
    def has_change_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)

admin.site.register(Schule, SchulAdmin)
admin.site.register(Schulart, SchulartAdmin)
admin.site.register(Wettbewerb)
admin.site.register(Beitrag, BeitragAdmin)
