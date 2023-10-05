from django.urls import path
from . import views

urlpatterns = [
    path("student/signup", views.student_signup, name="student_signup"),
    path("college/signup", views.college_signup, name="college_signup"),
    path("college/login", views.college_login, name="college_login"),
    path("student/login", views.student_login, name="student_login"),
]