from django.shortcuts import render, redirect

from .models import Post

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def blog(request):
	postlist = Post.objects.all()
	return render(request, 'main/blog.html', {'postlist':postlist})

def detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'main/detail.html', {'post':post})

def new(request):
	if request.method == 'POST':
		new_blog=Post.objects.create(
			postname = request.POST['postname'],
			contents = request.POST['contents'],
		)
		return blog(request)
	return render(request, 'main/new.html')

def delete(request, pk):
	post = Post.objects.get(pk=pk)
	post.delete()
	return redirect('/blog')
