from django.shortcuts import render, HttpResponse

# Create your views here.
def profile_view(request, username):
    return HttpResponse(f"Profile page of {username}")