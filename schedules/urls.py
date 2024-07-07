from django.urls import path
from .views import ScheduleListView, ScheduleDetailView

urlpatterns = [
    path('schedules/', ScheduleListView.as_view(), name='schedule-list'),
    path('schedules/<int:schedule_id>/', ScheduleDetailView.as_view(), name='schedule-detail'),
]