from django.shortcuts import render
from .models import Blog, Comment
# Create your views here.
def index(request):
	posts = Blog.objects.order_by('-posted')
	return render(request, 'blog/index.html',{'posts': posts [len(posts)-3:]})
