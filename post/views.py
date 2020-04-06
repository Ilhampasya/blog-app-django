from .models import Post
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'post/index.html', {
        'posts': Post.objects.order_by('-id').all()
    })
def read(request, id):
    return render(request, 'post/read.html', {
        'post': Post.objects.get(id=id)
    })