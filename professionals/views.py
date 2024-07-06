from professionals.models import Professionals
from professionals.serializers import ProfessionalsSerializer
from django.shortcuts import render
from rest_framework import generics # type: ignore


class ProfessionalView(generics.CreateAPIView):
    queryset = Professionals.objects.all()
    serializer_class = ProfessionalsSerializer

  
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class ProfessionalAllView(generics.ListAPIView):
    queryset = Professionals.objects.all()
    serializer_class = ProfessionalsSerializer



    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

class UserViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professionals.objects.all()
    serializer_class = ProfessionalsSerializer
    lookup_url_kwarg = "professional_id"

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)    

