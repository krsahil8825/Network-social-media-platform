from django.urls import path
from . import views

urlpatterns = [
    path("", views.feed_index, name="feed_index"),
    path("create/", views.create_post, name="create_post"),
    path("like/<slug:request_slug>/", views.like_post, name="like_post"),
    path("edit/<slug:request_slug>/", views.edit_post, name="edit_post"),
    path("delete/<slug:request_slug>/", views.delete_post, name="delete_post"),
]
