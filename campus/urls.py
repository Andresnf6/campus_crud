
from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render

urlpatterns = [
    path('', lambda request: render(request, "home.html")),
    path('admin/', admin.site.urls),
    path("attendance/", include("attendance.urls")),
    path("quizzes/", include("quizzes.urls")),
]