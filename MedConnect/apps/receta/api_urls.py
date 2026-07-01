from rest_framework.routers import DefaultRouter
from .views import RecetaViewSet

# Crea una instancia del DefaultRouter, que gestionará las rutas de la API
router = DefaultRouter()
router.register(r'recetas', RecetaViewSet, basename = 'recetas')

urlpatterns = router.urls