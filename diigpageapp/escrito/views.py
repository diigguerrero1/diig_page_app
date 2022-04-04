from email.mime import image
from multiprocessing import context
from django.shortcuts import render

from escrito.models import Post_escrito


def posts_gallery(request):

    total_posts = Post_escrito.objects.all()
    posts = total_posts.order_by('id').reverse()
    ultimate_post = total_posts.order_by('id').last()

    context = {
        'posts': posts,
        'ultimate_post': ultimate_post,
    }

    return render(request, "app/gallery_escrito.html", context)


def post_escrito(request, slug):

    post = Post_escrito.objects.get(
        slug = slug
    )

    context = {
        'post': post,
    }

    return render(request, "app/post_escrito.html", context)
