from django.shortcuts import render
from multimedia.models import Post_multimedia


def gallery_multimedia(request):

    total_posts = Post_multimedia.objects.all()
    posts = total_posts.order_by('id').reverse()
    ultimate_post = total_posts.order_by('id').last()

    context = {
        "posts": posts,
        "ultimate_post": ultimate_post,
    }

    return render(request, 'app/gallery_multimedia.html', context)

def post_multimedia(request, slug):

    post = Post_multimedia.objects.get(
        slug = slug
    )

    context = {
        'post': post,
    }

    return render(request, "app/post_multimedia.html", context)
