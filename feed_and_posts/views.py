from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Post, Comment

@login_required
def feed_index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed_and_posts/index.html', {'page_obj': page_obj})

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
