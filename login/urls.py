from django.urls import path
from . import views

urlpatterns = [
    path('accounts/', views.login, name='login'),
    path('', views.index, name='home'),
]
