from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_f),
    path('get-started', views.transcribe_f),
    path('category', views.category_f),
    path('work', views.work_f),
    path('login/', views.login_f, name='login'),
    path('logout/', views.logout_f, name='logout'),
    path('register', views.register, name='register'),
    path('login_homepage', views.login_homepage, name='login_homepage'),
    # path('login_about', views.login_about, name='login_about'),
]