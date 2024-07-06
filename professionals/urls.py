from django.urls import path
from . import views

urlpatterns = [
    path("professionals/", views.UserView.as_view()),
    path("professionals/all/", views.UserAllView.as_view()),
    path("professionals/<int:user_id>/", views.UserViewDetail.as_view()),
] 