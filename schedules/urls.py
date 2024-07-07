from django.urls import path
from . import views

urlpatterns = [
    path("schedules/", views.ScheduleCreateView.as_view(), name='schedule-create'),
    path("schedules/all/", views.ScheduleListView.as_view(), name='schedule-list'),
    path("schedules/<int:schedule_id>/", views.ScheduleDetailView.as_view(), name='schedule-detail'),
]
