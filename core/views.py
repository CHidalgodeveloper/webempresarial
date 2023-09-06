from django.shortcuts import render
# Create your views here.

"""
Inicio - home/
historia - about/
servicios - services/
visitanos - store/
Contacto - contact/
blog - blog/
politicas -sample/
"""

def home(request):
    return render(request,"core/index.html")
def about(request):
    return render(request,"core/about.html")

def store(request):
    return render(request,"core/store.html")


