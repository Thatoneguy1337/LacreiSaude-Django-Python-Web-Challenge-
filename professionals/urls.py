from django.urls import path
from . import views

urlpatterns = [
    path("professionals/", views.ProfessionalView.as_view()),
    path("professionals/all/", views.ProfessionalAllView.as_view()),
    path("professionals/<int:professional_id>/", views.ProfessionalViewDetail.as_view()),

] 