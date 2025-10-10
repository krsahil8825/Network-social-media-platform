from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed_index, name="feed_index"),
    path("create/", views.create_post, name="create_post"),
]
