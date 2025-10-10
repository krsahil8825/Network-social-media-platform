from django.shortcuts import render, HttpResponse


def profile_view(request, username):
    return HttpResponse(f"Profile page of {username}")