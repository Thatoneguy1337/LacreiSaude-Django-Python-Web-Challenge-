from rest_framework import serializers # type: ignore
from rest_framework.validators import UniqueValidator # type: ignore
from .models import Professionals




class ProfessionalsSerializer(serializers.ModelSerializer):

    fullname = serializers.CharField(
        validators = [
            UniqueValidator(
                queryset= Professionals.objects.all(),
                message= "A professional with that name already exists"
            )
        ]
    )

    def create(self, validated_data: dict) -> Professionals:
      
      
      return Professionals.objects.create_user(**validated_data)

    
    def update(self, instance: Professionals, validated_data: dict) -> Professionals:
        
        

        instance.save()

        return instance


    class Meta:
        model = Professionals
        fields = [
            "id",
            "fullname",
            "profession",
            "adress",
            "contact",
            "socialname",
        ]
        read_only_fields = ["id"]