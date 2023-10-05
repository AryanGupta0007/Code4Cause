from django.shortcuts import render
from .models import Student, College


def student_signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]
        conf_password = request.POST["conf-password"]
        college = request.POST["college"]
        university = request.POST["university"]
        course = request.POST["course"]
        year = request.POST["year"]
        mobile_no = request.POST["mobile-number"]
    

def student_login(request):
    pass


def college_signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        password = request.POST["password"]
        conf_password = request.POST["conf-password"]
        college = request.POST["college"]
        university = request.POST["university"]
        course = request.POST["course"]
        year = request.POST["year"]
        email = request.POST["email"]
        mobile_no = request.POST["mobile-number"]
        student = Student(
            name=name,
            username=username,
            password=password,
            college=college,
            university=university,
            course=course,
            year=year,
            email=email,
            mobile_no=mobile_no
        )
        student.save()

    return render(request, "userAuth/student_sign_up.html")


def college_login(request):
    pass