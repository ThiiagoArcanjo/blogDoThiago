from django.shortcuts import render
from django.utils import timezone
from .models import Post


def lista_post(request):
    posts = Post.objects.filter(data_de_publicacao__lte=timezone.now()).order_by('data_de_publicacao')
    return render(request, 'blog/lista_post.html', {'posts': posts})