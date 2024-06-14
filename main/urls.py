# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/update/', views.subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:pk>/delete/', views.user_delete, name='user_delete'),
    path('statistics/', views.statistics_view, name='statistics'),
    path('study-materials/', views.study_material_list, name='study_material_list'),
    path('study-materials/create/', views.study_material_create, name='study_material_create'),
    path('study-materials/<int:pk>/update/', views.study_material_update, name='study_material_update'),
    path('study-materials/<int:pk>/delete/', views.study_material_delete, name='study_material_delete'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('assignments/create/', views.assignment_create, name='assignment_create'),
    path('assignments/<int:pk>/update/', views.assignment_update, name='assignment_update'),
    path('assignments/<int:pk>/delete/', views.assignment_delete, name='assignment_delete'),
    path('achievements/', views.achievement_list, name='achievement_list'),
    path('achievements/create/', views.achievement_create, name='achievement_create'),
    path('achievements/<int:pk>/update/', views.achievement_update, name='achievement_update'),
    path('achievements/<int:pk>/delete/', views.achievement_delete, name='achievement_delete'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
    path('profile/delete/', views.profile_delete, name='profile_delete'),
]









