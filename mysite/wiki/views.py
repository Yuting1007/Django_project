from django.shortcuts import render


def wiki_home(request):
    return render(request, 'index.html')
