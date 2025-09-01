from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, ParticipanteViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'participantes', ParticipanteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

