from django.urls import path
from main import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.subject_create, name='subject_create'),
    path('subjects/<int:pk>/update/', views.subject_update, name='subject_update'),
    path('subjects/<int:pk>/delete/', views.subject_delete, name='subject_delete'),
    path('users/', views.user_list, name='user_list'),
    path('users/create/', views.user_create, name='user_create'),
    path('users/<int:pk>/update/', views.user_update, name='user_update'),
    path('users/<int:user_id>/delete/', views.user_delete, name='user_delete'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('teachers/stats/', views.statistics_view, name='teacher_stats'),
    path('teachers/<int:id>/subjects/', views.teacher_subject_detail, name='teacher_subject_detail'),
    path('teacher/subjects/', views.teacher_subjects, name='teacher_subjects'),
    path('subjects/create_view/', views.subject_create_view, name='subject_create_view'),
]






