from django.shortcuts import render


def index(request):
    name = "marcis"
    context = {"name": name}
    return render(request, 'base.html', context)
