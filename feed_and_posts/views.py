from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post, Comment

def feed_index(request):
    posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'feed_and_posts/index.html', {'page_obj': page_obj})
