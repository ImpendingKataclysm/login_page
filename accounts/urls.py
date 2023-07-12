from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('signup/', views.SignUpPage.as_view(), name='signup'),
    path('generate_password/', views.generate_password, name='generate_password')
]
