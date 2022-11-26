from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all() # We are taking all the objects from the database posts and saving it to the posts variable
    return render(request, 'index.html', {'posts': posts}) # Here we are passing the data into our template which is index.html

def post(request, pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts': posts})
