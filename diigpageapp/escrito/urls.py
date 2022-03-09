from .views import posts_gallery

from django.urls import path

app_name = 'Escrito'

urlpatterns = [
    path('gallery/', posts_gallery, name='gallery'),
]