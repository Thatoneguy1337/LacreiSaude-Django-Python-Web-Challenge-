from rest_framework import serializers
from .models import Schedules

class SchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = [
            "id",
            "professional",
            "appointment_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    