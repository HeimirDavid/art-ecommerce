from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .forms import UserLoginForm



# Create your views here.
def logout_view(request):
    """ Log the user out """
    logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login_view(request):
    if request.method == "POST":
        login_form  = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in")
            else: 
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    context = {'login_form':login_form}
    return render(request, 'login.html', context)

