from django.shortcuts import render

def home(request):
    return render(request, "app/index.html")

def diig(request):
    return render(request, "app/diig.html")