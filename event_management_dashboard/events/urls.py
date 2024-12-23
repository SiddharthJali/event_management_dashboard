from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.event_list, name='event_list'),
    path('events/create/', views.event_create_edit, name='event_create'),
    path('events/<int:pk>/edit/', views.event_create_edit, name='event_update'),
    path('events/<int:pk>/delete/', views.event_confirm_delete, name='event_delete'),

    path('attendees/', views.attendee_list, name='attendee_list'),
    path('attendees/create/', views.attendee_create_edit, name='attendee_create'),
    path('attendees/<int:pk>/edit/', views.attendee_create_edit, name='attendee_update'),
    path('attendees/<int:pk>/delete/', views.attendee_confirm_delete, name='attendee_delete'),

    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create_edit, name='task_create'),
    path('tasks/<int:pk>/edit/', views.task_create_edit, name='task_update'),
    path('tasks/<int:pk>/delete/', views.task_confirm_delete, name='task_delete'),

    path('', views.dashboard, name='dashboard'),
]
