from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(created_date=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

def index(request):
    return render(request,'blog/index.html',{})