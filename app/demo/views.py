from django.shortcuts import render


def index(request, model_name):
    return render(request, 'index.html')
