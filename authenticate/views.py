from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import User


# login handler
def login_view(request):
    if request.method == "POST":

        # read username
        username = request.POST["username"]
        username = username.strip() if username else ""
        if not username:
            # missing username
            return render(
                request,
                "authenticate/login.html",
                {"message": "Username is required."},
            )

        # read password
        password = request.POST["password"]
        password = password.strip() if password else ""
        if not password:
            # missing password
            return render(
                request,
                "authenticate/login.html",
                {"message": "Password is required."},
            )

        # authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # set session
            next_url = request.GET.get("next") or request.POST.get("next")
            return redirect(next_url if next_url else "core_index")
        else:
            # wrong credentials
            return render(
                request,
                "authenticate/login.html",
                {"message": "Invalid username and/or password."},
            )
    else:
        # GET -> show login page
        return render(request, "authenticate/login.html")


# logout handler
def logout_view(request):
    logout(request)  # clear session
    return HttpResponseRedirect(reverse("core_index"))


# registration handler
def register(request):
    if request.method == "POST":
        # username validation
        username = request.POST["username"]
        username = username.strip() if username else ""
        if not username:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Username is required."},
            )

        # email validation
        email = request.POST["email"]
        email = email.strip() if email else ""
        if not email:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Email is required."},
            )

        # password validation
        password = request.POST["password"]
        password = password.strip() if password else ""
        if not password:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Password is required."},
            )

        # password confirmation validation
        confirmation = request.POST["confirmation"]
        confirmation = confirmation.strip() if confirmation else ""
        if not confirmation:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Password confirmation is required."},
            )

        # ensure passwords match
        if password != confirmation:
            return render(
                request,
                "authenticate/register.html",
                {"message": "Passwords must match."},
            )

        # try creating user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            # username taken
            return render(
                request,
                "authenticate/register.html",
                {"message": "Username already taken."},
            )

        # auto-login after registration
        login(request, user)
        return HttpResponseRedirect(reverse("core_index"))
    else:
        # GET -> show registration page
        return render(request, "authenticate/register.html")
