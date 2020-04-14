from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.models import User

# Create your views here.

def account_view(request):
    name = {'name':request.user}
    return render (request, "UserPage/UserPage.html",name)


def home_view(request):
    return render (request, "homepage/homepage.html")