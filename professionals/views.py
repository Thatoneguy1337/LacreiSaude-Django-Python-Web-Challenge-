from professionals.models import Professionals
from professionals.serializers import ProfessionalsSerializer
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