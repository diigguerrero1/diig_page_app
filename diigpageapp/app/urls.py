from .views import home, diig

from django.urls import path

app_name = 'App'

urlpatterns = [
    path('', home, name = 'inicio'),
    path('diig/', diig, name = 'diig'),
]
