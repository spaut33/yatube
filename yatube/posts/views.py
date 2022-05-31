from django.http import HttpResponse


def index(request):
    """View of main page"""
    return HttpResponse('Main page')


def group_posts(request, slug=None):
    """Posts filtered by groups (slug)"""
    return HttpResponse(f'Group posts {slug}')