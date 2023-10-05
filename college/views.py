from django.shortcuts import render

def index(request):
    return render(request, "college/index.html")

def event_details(request):
    return render(request, "college/event_details.html")

def event_form(request):
    return render(request, "college/event_form.html")