from django.shortcuts import render

def feed_index(request):
    return render(request, 'feed_and_posts/index.html', {})
