from .views import posts_gallery, post_escrito

from django.urls import path

app_name = 'Escrito'

urlpatterns = [
    path('gallery/', posts_gallery, name='gallery'),
    path('<slug:slug>/', post_escrito, name='post_escrito')
]