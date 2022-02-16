from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post



def lista_post(request):
    posts = Post.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'blog/lista_post.html', {'posts': posts})

def post_detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalhes.html', {'post': post})