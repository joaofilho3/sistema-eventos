from django.contrib import admin
from .models import Evento, Lote, Ingresso

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local')
    search_fields = ('nome', 'local')
    list_filter = ('data',)


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'evento', 'data_inicio', 'data_fim')
    search_fields = ('nome', 'evento__nome')
    list_filter = ('evento',)


@admin.register(Ingresso)
class IngressoAdmin(admin.ModelAdmin):
    list_display = ('get_evento', 'lote', 'preco', 'quantidade')
    search_fields = ('lote__evento__nome',)
    list_filter = ('lote',)

    def get_evento(self, obj):
        return obj.lote.evento.nome
    get_evento.short_description = 'Evento'


