from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('questions/', views.question_view, name='questionnaire'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('mood/add/', views.mood_add, name='mood_add'),
    path('tasks/', views.tasks_list, name='tasks'),
    path('tasks/add/', views.task_add, name='task_add'),
    path('tasks/toggle/<int:pk>/', views.task_toggle, name='task_toggle'),
    path('tasks/delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('journal/', views.journal_list, name='journal'),
    path('journal/add/', views.journal_add, name='journal_add'),

    path('resources/', views.resources_view, name='resources'),

    # ⭐ ADD THIS NEW ROUTE ⭐
    path('resources/breathing/', views.breathing_videos, name='breathing_videos'),

    path('ml-predict/', views.ml_predict_view, name='ml_predict'),
    path('resources/breathing/', views.breathing_videos, name='breathing_videos'),

]
