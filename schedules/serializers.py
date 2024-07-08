from rest_framework import serializers
from .models import Schedules

class SchedulesSerializer(serializers.ModelSerializer):
    professional_name = serializers.SerializerMethodField()

    class Meta:
        model = Schedules
        fields = ['id', 'professional', 'professional_name', 'appointment_date', 'created_at', 'updated_at']

    def get_professional_name(self, obj):
        return obj.professional.fullname