from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Blog, Comment
from time import strftime
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def index(request):
	posts = Blog.objects.order_by('-posted')
	return render(request, 'blog/index.html',{'posts': posts [:3]})


def archive(request):
	posts = Blog.objects.order_by('-posted')
	return render(request, 'blog/index.html',{'posts': posts})


def tips(request):
	return render(request, 'blog/techtips.html', {'time': strftime('%c')})


def about(request):
	return render(request, 'blog/about.html', {'time': strftime('%c')})

def post(request, post_id):
	return render(request, 'blog/entry.html', {'post': get_object_or_404(Blog, pk=post_id)})

def comment(request, post_id):
	post = get_object_or_404(Blog, pk=post_id)
	try:
		name = request.POST.get('name', '')
		email = request.POST.get('email', '')
		content = request.POST.get('content', '')
	except(KeyError):
		return render(request, 'blog/entry.html',{'post': post, 'error': "something went wrong",})
	else:
		comment = Comment(blog=post, commenter=name, email=email, content=content, posted=timezone.now())
		comment.save()
	return HttpResponseRedirect(f'/blog/{post_id}/')
	
