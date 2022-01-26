from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="projectIndex"),
    path("<int:pk>/", views.project_detail, name="projectDetail")
]