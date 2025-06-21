from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("HOME 1")


def about(request):
    return HttpResponse("ABOUT 1")


def contact(request):
    return HttpResponse("CONTACT 1")
