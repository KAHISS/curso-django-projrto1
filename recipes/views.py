from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "recipes/home.html", context={
        "name": "João",
        "surname": "Silva",
    }, status=201)


def about(request):
    return render(request, "temp/temp.html")


def contact(request):
    return HttpResponse("CONTACT 1")
