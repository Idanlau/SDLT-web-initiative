from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import logout

# Create your views here.
def account_create_view(request):
    form = UserCreationForm(request.POST)

    if form.is_valid():
        user = form.save()
        form = UserCreationForm()
        Profile.objects.create(
            user= user,
        )
    else:
        print('not valid')

    content = {"form": form}

    return render (request, "registration/register.html",content)

def logout_view(request):
    logout(request)
    return redirect('/')
