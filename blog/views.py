from django.shortcuts import render
# from models we want to get our blog information
from .models import Blog

# Create your views here.
def allblog(request):
    # We need to get all the blogs and we're storing them in blog 
    blog = Blog.objects
    return render(request, 'blog/allblogs.html', {'blog': blog})
