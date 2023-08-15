from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi web personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about/">Acerca de</a></li>
        <li><a href="/portafolio/">Mi portafolio</a></li>
        <li><a href="/contacto/">Contacto</a></li>
    </ul>
"""

# Create your views here.
def home(request):
    html_responseve = (html_base +  "<h2>Portada</h2><p>Esta es la portada</p>")
    return HttpResponse(html_responseve)

def about(request):
    return HttpResponse(html_base +  "<h2>Acerca de</h2><p>Me llamo Sebastian y soy programador.</p>")

def portafolio(request):
    return HttpResponse(html_base +  "<h2>Mi portafolio</h2><p>Me llamo Sebastian y este es mi portafolio.</p>")

def contacto(request):
    return HttpResponse(html_base +  "<h2>Contacto</h2><p>Direccion #########.</p><p>Telefono ########.</p>")