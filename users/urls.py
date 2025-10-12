from django.urls import path
from . import views

urlpatterns = [
    path("<str:username>/", views.profile_view, name="user_profile"),
    path("<str:username>/edit/", views.edit_profile, name="edit_profile"),
]
