from django.shortcuts import render
from .models import Blog, Comment
from time import strftime
# Create your views here.

def index(request):
	posts = Blog.objects.order_by('-posted')
	return render(request, 'blog/index.html',{'posts': posts [len(posts)-3:]})


def archive(request):
	posts = Blog.objects.order_by('-posted')
	return render(request, 'blog/index.html',{'posts': posts})


def tips(request):
	return render(request, 'blog/techtips.html', {'time': strftime('%c')})


def about(request):
	return render(request, 'blog/about.html', {'time': strftime('%c')})

