from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_f),
    path('get-started', views.transcribe_f),
    path('category', views.category_f),
    path('work', views.work_f),
    path('login', views.login_f, name='login'),
    path('register', views.register, name='register'),
]