from .views import user_singup, user_login, user_logout

from django.urls import path

app_name = 'Users'

urlpatterns = [
    path('singup', user_singup, name='singup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]