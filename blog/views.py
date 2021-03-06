from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator

def lista_post(request):
    posts_list = Post.objects.all().order_by('data_de_publicacao')
    paginator = Paginator(posts_list, 2)
    
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/lista_post.html', {'posts': posts})

def post_detalhes(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detalhes.html', {'post': post})

def novo_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_de_publicacao = timezone.now()
            post.save()
            return redirect('post_detalhes', pk=post.pk)
    
    else:
        form = PostForm()

    return render(request, 'blog/post_edite.html', {'form': form})

def post_edite(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_de_publicacao = timezone.now()
            post.save()
            return redirect('post_detalhes', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edite.html', {'form' : form})

def excluir_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('lista_post')


def confirmar_exclusao(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/confirmar_exclusao.html', {'post': post})

def hi(request):
    return render(request, 'blog/hi.html')
