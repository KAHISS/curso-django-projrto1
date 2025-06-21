from django.shortcuts import render


def home(request):
    return render(request, "recipes/home.html", context={
        "name": "João",
        "surname": "Silva",
    }, status=201)
