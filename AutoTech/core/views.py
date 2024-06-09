from django.shortcuts import render

# Create your views here.

def render_app(request):
    context = { }
    return render(request, "index.html", context)
