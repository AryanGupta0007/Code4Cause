from django.urls import path
from . import views 

urlpatterns=[
    path("", views.index, name="college_home"), 
    path("event_details/",views.event_details, name="event_details"),
    path("event_form/", views.event_form, name="event_form")
]
