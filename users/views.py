import profile
from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from feed_and_posts.models import Post
from .models import User, Profile, Follow
from .utils import is_image_url


@login_required
def edit_profile(request, username):
    if request.user.username != username:
        return redirect("404")
    if request.user.username == username:
        _, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        profile = get_object_or_404(Profile, user=request.user)

        avatar_link = request.POST.get("title")
        avatar_link = avatar_link.strip() if avatar_link else ""

        bio = request.POST.get("content")
        bio = bio.strip() if bio else ""

        if len(bio) > 250:
            return render(
                request,
                "users/edit_profile.html",
                {"profile": profile, "message": "Bio must be 250 characters or less."},
            )

        if avatar_link and not is_image_url(avatar_link):
            return render(
                request,
                "users/edit_profile.html",
                {"profile": profile, "message": "Please enter a valid image URL."},
            )

        try:
            profile.avatar_link = avatar_link
            profile.bio = bio
            profile.save()
        except ValidationError as e:
            print("Profile update error:", e)
            return render(
                request,
                "users/edit_profile.html",
                {"profile": profile, "message": "Invalid data provided."},
            )

        return redirect("user_profile", username=request.user.username)

    profile = get_object_or_404(Profile, user=request.user)
    return render(request, "users/edit_profile.html", {"profile": profile})


@login_required
def profile_view(request, username):
    if not User.objects.filter(username=username).exists():
        return redirect("404")

    this_user = User.objects.get(username=username)
    posts = Post.objects.filter(user=this_user).order_by("-created_at")
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if not Profile.objects.filter(user=this_user).exists():
        this_user_profile, created = Profile.objects.get_or_create(user=this_user)
    else:
        this_user_profile = get_object_or_404(Profile, user=this_user)

    if not Follow.objects.filter(follower=request.user, following=this_user).exists():
        is_following = False
    else:
        is_following = get_object_or_404(
            Follow, follower=request.user, following=this_user
        )
    return render(
        request,
        "users/index.html",
        {
            "this_user": this_user,
            "page_obj": page_obj,
            "this_user_profile": this_user_profile,
            "is_following": is_following,
        },
    )
