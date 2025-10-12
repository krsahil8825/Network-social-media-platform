from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import User


# this help to create login functionality
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        if not username:
            return render(
                request,
                "authenticate/login.html",
                {"message": "Username is required."},
            )
        password = request.POST["password"]

        if not password:
            return render(
                request,
                "authenticate/login.html",
                {"message": "Password is required."},
            )
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next") or request.POST.get("next")
            return redirect(next_url if next_url else "core_index")
        else:
            return render(
                request,
                "authenticate/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        return render(request, "authenticate/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("core_index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]

        if not username:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Username is required."},
            )

        email = request.POST["email"]

        if not email:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Email is required."},
            )
        password = request.POST["password"]

        if not password:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Password is required."},
            )

        confirmation = request.POST["confirmation"]

        if not confirmation:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Password confirmation is required."},
            )

        # Ensure password matches confirmation
        if password != confirmation:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Passwords must match."},
            )
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Username already taken."},
            )
        login(request, user)
        return HttpResponseRedirect(reverse("core_index"))
    else:
        return render(request, "authenticate/register.html")
