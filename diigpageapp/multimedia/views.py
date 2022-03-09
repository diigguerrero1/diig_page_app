from django.shortcuts import render

def gallery_multimedia(request):
    return render(request, 'app/gallery_multimedia.html')
