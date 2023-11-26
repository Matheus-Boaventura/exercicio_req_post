from django.urls import path
from app_aula5.views import home

urlpatterns = [
    path('', home)
]