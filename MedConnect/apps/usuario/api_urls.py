from django.urls import path
from .views import login_api, registro_api, logout_api

urlpatterns = [
    path('login/', login_api),
    path('registro/', registro_api),
    path('logout/', logout_api),
]