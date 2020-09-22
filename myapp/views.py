from django.shortcuts import render


def index(request):
    context = {
        'heading': 'Selamat Datang Di Website KC'
    }
    return render(request, 'index.html', context)
