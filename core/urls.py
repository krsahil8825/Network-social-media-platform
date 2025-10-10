from django.urls import path
from . import views


# URL patterns for the core app
urlpatterns = [
    path("", views.index, name="core_index"),
    path("about/", views.about, name="core_about"),
    path("contact/", views.contact, name="core_contact"),
]
