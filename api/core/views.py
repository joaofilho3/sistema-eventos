from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à API de Eventos!")

from rest_framework import viewsets
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer
