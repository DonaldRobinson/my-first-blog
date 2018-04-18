from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if (post.pk == 1):
        return render(request, 'blog/post_garfield.html', {'post': post, 'posts': posts})    

    if (post.pk == 2):
        return render(request, 'blog/garfield.html', {'post': post, 'posts': posts})    
    
def gfield_list(request):
    gfield = Post.objects.filter(title='Garfield') 
    return render(request, 'blog/garfield.html', {'gfield': gfield})   
