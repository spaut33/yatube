from django.shortcuts import render

from .models import Post


def index(request):
    """View of main page"""
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    context = {
        'title': 'Главная страница',
        'text': 'Это главная страница проекта Yatube',
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug=None):
    """Posts filtered by groups (slug)"""
    template = 'posts/group_list.html'
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
        'text': 'Здесь будет информация о группах проекта Yatube',
    }
    return render(request, template, context)
