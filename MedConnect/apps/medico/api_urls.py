from rest_framework.routers import DefaultRouter
from .views import MedicoViewSet

router = DefaultRouter()
router.register(r'medicos', MedicoViewSet, basename='medicos')

urlpatterns = router.urls