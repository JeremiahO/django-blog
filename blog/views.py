from django.shortcuts import render, get_object_or_404
# from models we want to get our blog information
from .models import Blog

# Create your views here.
def allblog(request):
    # We need to get all the blogs and we're storing them in blog
    blogs = Blog.objects
    return render(request, 'blog/allblogs.html', {'blogs': blogs})

def detail (request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detailblog})
