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

    
    def create(self, validated_data: dict) -> Schedules:
        return Schedules.objects.create(**validated_data)

    def update(self, instance: Schedules, validated_data: dict) -> Schedules:
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance    