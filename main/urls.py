from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Змінено user_login на login_view
    path('', views.home, name='home'),
]
