from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment
from users.models import Follow


@login_required
def post_inedex(request):
    # Redirect post index to main feed
    return redirect("feed_index")


@login_required
def feed_index(request):
    # Fetch all posts (newest first)
    posts = Post.objects.all().order_by("-created_at")
    # Paginate results
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # Render main feed
    return render(request, "feed_and_posts/index.html", {"page_obj": page_obj})


@login_required
def following_feed(request):
    # Get all users the current user follows
    following_users = Follow.objects.filter(follower=request.user).values_list(
        "following", flat=True
    )
    # Fetch posts only by followed users
    posts = Post.objects.filter(user__in=following_users).order_by("-created_at")
    paginator = Paginator(posts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # Render following feed
    return render(request, "feed_and_posts/following_feed.html", {"page_obj": page_obj})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    # Only the comment owner can edit
    if request.user != comment.user:
        return redirect("404")

    if request.method == "POST":
        content = request.POST.get("content")
        content = content.strip() if content else ""

        # Prevent empty comment
        if content:
            comment.content = content
            comment.save()
            return redirect("comment_on_post", request_slug=comment.post.slug)
        else:
            return render(
                request,
                "feed_and_posts/edit_comment.html",
                {
                    "comment": comment,
                    "message": "Comment cannot be empty.",
                },
            )

    return render(
        request,
        "feed_and_posts/edit_comment.html",
        {"comment": comment},
    )


@login_required
def delete_comment(request, comment_id):
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=comment_id)

        # Only the comment owner can delete
        if request.user != comment.user:
            return redirect("404")

        post_slug = comment.post.slug
        comment.delete()
        return redirect("comment_on_post", request_slug=post_slug)
    if request.method == "GET":
        comment = get_object_or_404(Comment, id=comment_id)

        # Only the comment owner can delete
        if request.user != comment.user:
            return redirect("404")

        return render(
            request,
            "feed_and_posts/delete_comment.html",
            {"comment": comment},
        )


@login_required
def comment_on_post(request, request_slug):
    # Check if post exists
    if not Post.objects.filter(slug=request_slug).exists():
        return redirect("404")

    post = get_object_or_404(Post, slug=request_slug)
    comments = Comment.objects.filter(post=post).order_by("-created_at")

    if request.method == "POST":
        content = request.POST.get("content")
        content = content.strip() if content else ""

        # Prevent empty comment
        if content:
            Comment.objects.create(user=request.user, post=post, content=content)
            return redirect("comment_on_post", request_slug=request_slug)
        else:
            return render(
                request,
                "feed_and_posts/comment_on_post.html",
                {"post_as_array": [post], "message": "Comment cannot be empty."},
            )

    # Render post with comments
    return render(
        request,
        "feed_and_posts/comment_on_post.html",
        {"post_as_array": [post], "comments": comments},
    )


@login_required
def delete_post(request, request_slug):
    # Validate post existence
    if not Post.objects.filter(slug=request_slug).exists():
        return redirect("404")

    post = get_object_or_404(Post, slug=request_slug)

    # Only the owner can delete
    if request.user != post.user:
        return redirect("404")

    if request.method == "POST":
        post.delete()
        return redirect("feed_index")

    return render(request, "feed_and_posts/delete_post.html", {"post_as_array": [post]})


@login_required
def edit_post(request, request_slug):
    # Fetch post or return 404
    post = get_object_or_404(Post, slug=request_slug)

    # Only owner can edit
    if request.user != post.user:
        return redirect("404")

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        title = title.strip() if title else ""
        content = content.strip() if content else ""

        # Validate title
        if title and len(title) <= 255:
            post.title = title
        else:
            return render(
                request,
                "feed_and_posts/edit_post.html",
                {
                    "post": post,
                    "message": "Title cannot be empty or exceed 255 characters.",
                },
            )

        # Validate content
        if content:
            post.content = content
        else:
            return render(
                request,
                "feed_and_posts/edit_post.html",
                {"post": post, "message": "Content cannot be empty."},
            )

        post.save()
        return redirect("feed_index")

    return render(request, "feed_and_posts/edit_post.html", {"post": post})


@login_required
@csrf_exempt
def like_post(request, request_slug):
    # Handle like/unlike via AJAX
    if request.method == "POST":
        try:
            post = get_object_or_404(Post, slug=request_slug)
            user = request.user

            # Toggle like
            if user in post.likes.all():
                post.likes.remove(user)
                liked = False
            else:
                post.likes.add(user)
                liked = True

            return JsonResponse(
                {"liked": liked, "total_likes": post.likes.count()}, status=200
            )

        except Exception as e:
            print(f"Error liking post: {e}")
            return JsonResponse(
                {"error": "An error occurred while processing your request."},
                status=500,
            )


@login_required
def create_post(request):
    # Redirect unauthenticated users (double check)
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        try:
            user = request.user
            title = request.POST.get("title")
            content = request.POST.get("content")

            title = title.strip() if title else ""
            content = content.strip() if content else ""

            # Prevent exact duplicate posts
            if Post.objects.filter(user=user, title=title, content=content).exists():
                return render(
                    request,
                    "feed_and_posts/create_post.html",
                    {"message": "Post with this title and content already exists."},
                )

            # Validate title length
            if title and len(title) > 255:
                return render(
                    request,
                    "feed_and_posts/create_post.html",
                    {"message": "Title cannot exceed 255 characters."},
                )

            # Final validation
            if content and title:
                Post.objects.create(user=user, title=title, content=content)
            else:
                return render(
                    request,
                    "feed_and_posts/create_post.html",
                    {"message": "Title and content cannot be empty."},
                )

            return redirect("feed_index")

        except Exception as e:
            print(f"Error creating post: {e}")
            return render(
                request,
                "feed_and_posts/create_post.html",
                {"message": "An error occurred while creating the post."},
            )

    # Render empty form
    return render(request, "feed_and_posts/create_post.html")