from django.shortcuts import get_object_or_404, render

from .models import Group, Post


def index(request):
    """Главная страница"""
    # Получаем 10 постов с сортировкой по дате
    # TODO: ordering наверное лучше вынести в Meta и убрать order_by тут и ниже
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': 'Последние обновления на сайте',
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug=None):
    """Posts filtered by groups (slug)"""
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
