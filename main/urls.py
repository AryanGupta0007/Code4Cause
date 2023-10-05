from django.urls import path
from . import views 

urlpatterns = [
    path("index/", views.index, name="main_home"),
    path("about_us/", views.about_us, name="about_us")
]