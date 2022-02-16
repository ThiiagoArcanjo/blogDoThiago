from django.shortcuts import render

def lista_post(request):
    return render(request, 'blog/lista_post.html', {})