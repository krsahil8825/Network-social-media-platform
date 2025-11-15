from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_inedex, name="post_index"),
    path("create/", views.create_post, name="create_post"),
    path("like/<slug:request_slug>/", views.like_post, name="like_post"),
    path("edit/<slug:request_slug>/", views.edit_post, name="edit_post"),
    path("<slug:request_slug>/delete/", views.delete_post, name="delete_post"),
    path("<slug:request_slug>/comment/", views.comment_on_post, name="comment_on_post"),
]
