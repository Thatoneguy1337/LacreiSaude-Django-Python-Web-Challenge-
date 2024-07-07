from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Schedules
from .serializers import SchedulesSerializer

class ScheduleFilter(filters.FilterSet):
    professional_id = filters.NumberFilter(field_name="professional__id")

    class Meta:
        model = Schedules
        fields = ['professional_id']

class ScheduleListView(generics.ListCreateAPIView):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ScheduleFilter

class ScheduleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedules.objects.all()
    serializer_class = SchedulesSerializer
    lookup_url_kwarg = "schedule_id"










