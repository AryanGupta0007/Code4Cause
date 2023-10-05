from django.urls import path
from . import views 

urlpatterns=[
    path("", views.index, name="college_home"), 
    path("event_details/",views.index, name="event_details"),
    path("event_form/", views.index, name="event_form")
]
