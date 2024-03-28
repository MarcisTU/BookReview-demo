from django.shortcuts import render


def index(request):
    name = "marcis"
    context = {"name": name}
    return render(request, 'base.html', context)

def book_search(request):
    search_text = request.GET.get("search", "")
    search_context = {"search_text": search_text}
    return render(request, 'search-results.html', search_context)
