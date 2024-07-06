from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Professionals

class ProfessionalsSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=Professionals.objects.all(),
                message="A professional with that name already exists"
            )
        ]
    )

    class Meta:
        model = Professionals
        fields = [
            "id",
            "fullname",
            "profession",
            "address",
            "contact",
            "socialname",
        ]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> Professionals:
        return Professionals.objects.create(**validated_data)

    def update(self, instance: Professionals, validated_data: dict) -> Professionals:
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance