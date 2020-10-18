from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.index, name="index"),
    path("dataset/<int:pk>/", views.dataset, name="dataset"),
    path("download/", views.download, name="download"),
]
