from django.urls import path
from django.contrib import admin
from .views import StudentView

urlpatterns = [
    path("students/", StudentView.as_view()),
    path("students/<int:pk>/", StudentView.as_view())
]
