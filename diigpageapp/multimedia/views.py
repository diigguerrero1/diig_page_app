from django.shortcuts import render
from multimedia.models import Post_multimedia


def gallery_multimedia(request):

    posts = Post_multimedia.objects.all()

    context = {
        "posts": posts
    }

    return render(request, 'app/gallery_multimedia.html', context)
