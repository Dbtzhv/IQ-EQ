from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TestLoginView, IQTestResultView, EQTestResultView


urlpatterns = [
    path('test/', TestLoginView.as_view()),
    path('iq/', IQTestResultView.as_view()),
    path('eq/', EQTestResultView.as_view()),
]