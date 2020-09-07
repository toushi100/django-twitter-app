from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .models import Comment



def home (request):
    content = {
        'posts': Post.objects.all()
    }
    return render(request , 'Blogapp/home.html', content)

def about (request):
    return render(request,'Blogapp/about.html', {'title' : 'about'})