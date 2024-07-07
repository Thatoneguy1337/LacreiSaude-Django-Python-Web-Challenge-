from django.urls import path
from . import views

urlpatterns = [
    path("professionals/", views.ProfessionalView.as_view(), name='professional-create' ),
    path("professionals/all/", views.ProfessionalAllView.as_view(), name ='professional-list'),
    path("professionals/<int:professional_id>/", views.ProfessionalViewDetail.as_view(), name='professional-detail' ),

] 