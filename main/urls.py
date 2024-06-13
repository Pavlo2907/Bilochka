from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('teacher_subjects/', views.teacher_subjects, name='teacher_subjects'),
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
    path('study_materials/create/', views.study_material_create, name='study_material_create'),
    path('subjects/<int:subject_id>/study_materials/', views.study_material_list, name='study_material_list'),
    path('assignments/create/', views.assignment_create, name='assignment_create'),
    path('achievements/create/', views.achievement_create, name='achievement_create'),
]







