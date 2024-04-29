from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_f),
    path('get-started', views.transcribe_f),
]