from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Post, Comment


@login_required
def post_inedex(request):
    return redirect('feed_index')

@login_required
def feed_index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed_and_posts/index.html', {'page_obj': page_obj})


@login_required
def comment_on_post(request, request_slug):
    if not Post.objects.filter(slug=request_slug).exists():
        return redirect('404')
    
    post = get_object_or_404(Post, slug=request_slug)
    comments = Comment.objects.filter(post=post).order_by('-created_at')

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(user=request.user, post=post, content=content)
            return redirect('comment_on_post', request_slug=request_slug)
        else:
            return render(request, 'feed_and_posts/comment_on_post.html', {'post_as_array': [ post], 'message': 'Comment cannot be empty.'})

    return render(request, 'feed_and_posts/comment_on_post.html', {'post_as_array': [post], 'comments': comments})

@login_required
def delete_post(request, request_slug):
    if not Post.objects.filter(slug=request_slug).exists():
        return redirect('404')
    
    post = get_object_or_404(Post, slug=request_slug)

    if request.user != post.user:
        return redirect('404')

    if request.method == 'POST':
        post.delete()
        return redirect('feed_index')

    return render(request, 'feed_and_posts/delete_post.html', {'post_as_array': [post]})

@login_required
def edit_post(request, request_slug):
    post = get_object_or_404(Post, slug=request_slug)

    if request.user != post.user:
        return redirect('404')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and len(title) <= 255:
            post.title = title
        else:
            return render(request, 'feed_and_posts/edit_post.html', {'post': post, 'message': 'Title cannot be empty or exceed 255 characters.'})

        if content:
            post.content = content
        else:
            return render(request, 'feed_and_posts/edit_post.html', {'post': post, 'message': 'Content cannot be empty.'})

        post.save()
        return redirect('feed_index')

    return render(request, 'feed_and_posts/edit_post.html', {'post': post})


@login_required
@csrf_exempt
def like_post(request, request_slug):
    if request.method == 'POST':
        try:
            post = get_object_or_404(Post, slug=request_slug)
            user = request.user

            if user in post.likes.all():
                post.likes.remove(user)
                liked = False
            else:
                post.likes.add(user)
                liked = True

            return JsonResponse({'liked': liked, 'total_likes': post.likes.count()}, status=200)
        except Exception as e:
            print(f"Error liking post: {e}")
            return JsonResponse({'error': 'An error occurred while processing your request.'}, status=500)

@login_required
def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Handle post creation
    if request.method == 'POST':
        # Basic validation
        try:
            # Get user input
            user = request.user
            title = request.POST.get('title')
            content = request.POST.get('content')

            # Check for duplicate posts by the same user with the same title and content
            if Post.objects.filter(user=user, title=title, content=content).exists():
                return render(request, 'feed_and_posts/create_post.html', {'message': 'Post with this title and content already exists.'})

            # Validate title length
            if title and len(title) > 255:
                return render(request, 'feed_and_posts/create_post.html', {'message': 'Title cannot exceed 255 characters.'})
            
            # Create the post if valid
            if content and title:
                Post.objects.create(user=user, title=title, content=content)
            else:
                return render(request, 'feed_and_posts/create_post.html', {'message': 'Title and content cannot be empty.'})
            return redirect('feed_index')
        
        # Catch any unexpected errors
        except Exception as e:
            print(f"Error creating post: {e}")
            return render(request, 'feed_and_posts/create_post.html', {'message': 'An error occurred while creating the post.'})
        
    return render(request, 'feed_and_posts/create_post.html')
