from django.views.generic import DetailView, ListView
from django.http import FileResponse,HttpResponse
from .models import Post
from django.shortcuts import render


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

def index(request):
    template='base.html'
    return render(request,template)
