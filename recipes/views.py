from django.shortcuts import render


def home(request):
    return render(request, "recipes/pages/home.html", context={
        "name": "João",
        "surname": "Silva",
    }, status=201)


def recipe(request, id):
    return render(request, "recipes/pages/home.html", context={
        "name": "João",
        "surname": "Silva",
    }, status=201)
