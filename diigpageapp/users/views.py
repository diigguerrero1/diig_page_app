from django.shortcuts import render


def user_singup(request):
    return render(request, 'app/singup.html')


def user_login(request):
    return render(request, 'app/login.html')


def user_logout(request):
    return render(request, 'app/logout.html')
