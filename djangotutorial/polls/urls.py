from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dokimi" ,views.Myhtml , name="s")
]