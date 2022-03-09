from django.shortcuts import render

def posts_gallery(request):
    return render(request, "app/gallery_escrito.html")

def post_escrito(request):
    return render(request, "app/post_escrito.html")
