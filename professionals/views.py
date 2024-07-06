from professionals.models import Professionals
from professionals.serializers import ProfessionalsSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics


class ProfessionalView(generics.CreateAPIView):
    queryset = Professionals.objects.all()
    serializer_class = ProfessionalsSerializer

class ProfessionalAllView(generics.ListAPIView):
    queryset = Professionals.objects.all()
    serializer_class = ProfessionalsSerializer

class ProfessionalViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professionals.objects.all()
    serializer_class = ProfessionalsSerializer
    lookup_url_kwarg = "professional_id"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


