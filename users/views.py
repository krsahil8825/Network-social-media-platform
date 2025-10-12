from django.shortcuts import render


def profile_view(request, username):
    return render(request, "users/index.html", {"username": username})