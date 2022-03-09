from .views import gallery_multimedia

from django.urls import path

app_name = 'Multimedia'

urlpatterns = [
    path('multimedia/', gallery_multimedia, name='multi_gallery')
]