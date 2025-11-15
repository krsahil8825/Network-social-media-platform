from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from feed_and_posts.models import Post
from .models import User, Profile, Follow
from .utils import is_image_url


@login_required
@csrf_exempt
def follow_toggle(request, username):
    # Only allow POST
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request method."}, status=400)

    # Block self-follow
    if request.user.username == username:
        return JsonResponse({"error": "You cannot follow yourself."}, status=400)

    # Validate target user
    if not User.objects.filter(username=username).exists():
        return JsonResponse({"error": "User does not exist."}, status=404)

    follow_user = get_object_or_404(User, username=username)
    follower = request.user

    # Toggle follow/unfollow
    if Follow.objects.filter(follower=follower, following=follow_user).exists():
        follow_instance = get_object_or_404(
            Follow, follower=follower, following=follow_user
        )
        follow_instance.delete()
        return JsonResponse(
            {"status": "unfollowed", "message": f"You have unfollowed {username}."},
            status=200,
        )
    else:
        Follow.objects.create(follower=follower, following=follow_user)
        return JsonResponse(
            {"status": "followed", "message": f"You are now following {username}."},
            status=200,
        )


@login_required
def edit_profile(request, username):
    # Only allow user to edit own profile
    if request.user.username != username:
        return redirect("404")

    # Ensure profile exists
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":

        # Get avatar URL
        avatar_link = request.POST.get("title")
        avatar_link = avatar_link.strip() if avatar_link else ""

        # Get bio
        bio = request.POST.get("content")
        bio = bio.strip() if bio else ""

        # Validate bio length
        if len(bio) > 250:
            return render(
                request,
                "users/edit_profile.html",
                {"profile": profile, "message": "Bio must be 250 characters or less."},
            )

        # Check avatar URL is valid image
        if avatar_link and not is_image_url(avatar_link):
            return render(
                request,
                "users/edit_profile.html",
                {"profile": profile, "message": "Please enter a valid image URL."},
            )

        try:
            # Save updates
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

    # Initial GET render
    return render(request, "users/edit_profile.html", {"profile": profile})


@login_required
def profile_view(request, username):
    # Ensure user exists
    if not User.objects.filter(username=username).exists():
        return redirect("404")

    this_user = User.objects.get(username=username)

    # Fetch posts for profile
    posts = Post.objects.filter(user=this_user).order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    # Ensure profile exists
    this_user_profile, _ = Profile.objects.get_or_create(user=this_user)

    # Determine follow status
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
