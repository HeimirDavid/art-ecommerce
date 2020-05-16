from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserLoginForm, UserRegistrationForm


@login_required
def logout_view(request):
    """ Log the user out """
    logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login_view(request):
    if request.user.is_authenticated:
        messages.success(request, "You are already logged in")
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = authenticate(username=request.POST['username'],
                                password=request.POST['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in")
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()

    context = {'login_form': login_form}
    return render(request, 'login.html', context)


def register_user(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = authenticate(username=request.POST['username'],
                                password=request.POST['password1'])
            if user is not None:
                login(request, user)
                messages.success(
                    request,
                    "You have succesfully registered and are now logged in")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account")
    else:
        registration_form = UserRegistrationForm()

    context = {'registration_form': registration_form}
    return render(request, 'registration.html', context)
