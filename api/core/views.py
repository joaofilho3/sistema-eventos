from rest_framework import viewsets, permissions
from .models import Evento, Lote, Ingresso
from .serializers import EventoSerializer, LoteSerializer, IngressoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [permissions.AllowAny]

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
    permission_classes = [permissions.AllowAny]

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(comprador=self.request.user)

from django.shortcuts import render
from .models import Evento

def eventos_front(request):
    eventos = Evento.objects.all()
    return render(request, 'core/eventos.html', {'eventos': eventos})
