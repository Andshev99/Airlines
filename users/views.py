from django.shortcuts import render
from django.http import HttpResponse

# Створіть свої вікна тут.

def index(request):
    return HttpResponse("Users")