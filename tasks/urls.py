from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('<int:pk>/', views.task_detail, name='task-detail'),
    path('new/', views.task_create, name='task-create'),
    path('<int:pk>/edit/', views.task_update, name='task-update'),

]