from django.urls import path

from .views import (
    EventListCreateView, EventRetrieveUpdateDestroyView,
    AttendeeListCreateView, AttendeeRetrieveUpdateDestroyView,
    TaskListCreateView, TaskRetrieveUpdateDestroyView
)

urlpatterns = [
    # Event URLs
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-detail'),
    
    # Attendee URLs
    path('attendees/', AttendeeListCreateView.as_view(), name='attendee-list-create'),
    path('attendees/<int:pk>/', AttendeeRetrieveUpdateDestroyView.as_view(), name='attendee-detail'),
    
    # Task URLs
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]
