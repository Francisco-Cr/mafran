#import json
from django.shortcuts import render
#from django.views.generic import ListView
from .models import Ferreteria,Adhesivo,Aseo
from django.core.paginator import Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def buscar(request):
    if request.method == "POST":
        busqueda = request.POST['busqueda']
        producto = Aseo.objects.filter(nombre__contains=busqueda) or Ferreteria.objects.filter(nombre__contains=busqueda) or Adhesivo.objects.filter(nombre__contains=busqueda)
        return render(request,'core/buscar.html', 
            {'results':producto,'busqueda':busqueda})
    else:
        return render(request,'core/buscar.html')
    
'''''
En la linea 8: si no funciona de debe usar con (), envez de []
En la linea 9: se ponen los modelos a utilizar
En la linea 11: Es donde se busca el modelo donde se esta trabajando y se retorna en la Linea 13
'''''
        
def home(request):
    return render(request,'core/nosotros.html')

def aseo(request):
    aseo_list=Aseo.objects.all()
    paginator = Paginator(aseo_list, 6)

    page = request.GET.get('page')
    try:
        producto = paginator.page(page)
    except PageNotAnInteger:
        #Si la página no es un número entero, muestra la primera página
        producto = paginator.page(1)
    except EmptyPage:
        #Si la página está fuera de rango (página 9999), muestra la última página
        producto = paginator.page(paginator.num_pages)
    return render(request,'core/aseoCat.html',{"aseo":producto})


def ferreteria(request):
    ferreteria_list=Ferreteria.objects.all()
    paginator = Paginator(ferreteria_list, 8)

    page = request.GET.get('page')
    try:
        producto = paginator.page(page)
    except PageNotAnInteger:
        producto = paginator.page(1)
    except EmptyPage:
        producto = paginator.page(paginator.num_pages)
    return render(request,'core/ferrCat.html',{"ferreteria":producto})


def adhesivos(request):
    adhesivo_list=Adhesivo.objects.all()
    paginator = Paginator(adhesivo_list, 8)

    page = request.GET.get('page')
    try:
        producto = paginator.page(page)
    except PageNotAnInteger:

        producto = paginator.page(1)
    except EmptyPage:
    
        producto = paginator.page(paginator.num_pages)
    return render(request,'core/adhesivos.html',{"adhesivo":producto})