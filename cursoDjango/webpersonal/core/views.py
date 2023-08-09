from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    html_responseve = "<h1>Portada</h1>"
    for i in range(8):
        html_responseve += "<h2>lista</h2>"
    return HttpResponse(html_responseve)