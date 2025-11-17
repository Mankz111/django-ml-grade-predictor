from django.urls import path
from . import views

urlpatterns = [
    path("", views.predictor_view, name="index"),
]