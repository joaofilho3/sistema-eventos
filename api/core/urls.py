from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventoViewSet, LoteViewSet, IngressoViewSet

router = DefaultRouter()
router.register(r'eventos', EventoViewSet)
router.register(r'lotes', LoteViewSet)
router.register(r'ingressos', IngressoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

