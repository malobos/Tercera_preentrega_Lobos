from django.shortcuts import render
from django.http import HttpResponse
from App1.models import *
from App1.forms import *
# Create your views here.

#VISTAS INICIALES DE CADA MODELO
def inicio(request):
    return render(request, "App1/inicio.html" )

def vrecCarne(request):
    return render(request, "App1/recetasCarne.html" )

def vrecVerduras(request):
    return render(request, "App1/recetasVerduras.html" )

def vrecPastas (request):
    return render(request, "App1/recetasPastas.html" )

def vcontacto (request):
    return render(request, "App1/contacto.html" )

#VISTA DE REGISTRO EXITOSO
def vregExitoso(request):
    return render(request, "App1/regExitoso.hmtl")
#VISTAS DE FORMULARIOS DE CARGA DE DATOS
#VERDURAS
def recVerduraForm(request):
 
      if request.method == "POST":
 
            miFormulario = frecVerduras(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  recetaV1 = recVerduras(nombre=informacion["nombre"], fechaDeSubida=informacion["fechaDeSubida"], ingredientes= informacion["ingredientes"] )
                  recetaV1.save()
                  return render(request, "App1/regExitoso.html")
      else:
            miFormulario = frecVerduras()
 
      return render(request, "App1/formRecVerdura.html", {"miFormulario": miFormulario})
#CARNES
def recCarneForm(request):
 
      if request.method == "POST":
 
            miFormulario = frecCarne(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  recetaC1 = recCarne(nombre=informacion["nombre"], fechaDeSubida=informacion["fechaDeSubida"], ingredientes= informacion["ingredientes"] )
                  recetaC1.save( )
                  return render(request, "App1/regExitoso.html")
      else:
            miFormulario = frecCarne()
 
      return render(request, "App1/formRecCarne.html", {"miFormulario": miFormulario})
#PASTAS
def recPastasForm(request):
 
      if request.method == "POST":
 
            miFormulario = frecPastas(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  recetaP1 = recPastas(nombre=informacion["nombre"], fechaDeSubida=informacion["fechaDeSubida"], ingredientes= informacion["ingredientes"] )
                  recetaP1.save( )
                  return render(request, "App1/regExitoso.html")
      else:
            miFormulario = frecPastas()
 
      return render(request, "App1/formRecPastas.html", {"miFormulario": miFormulario})
#CONTACTO
def ContactoForm(request):
 
      if request.method == "POST":
 
            miFormulario = fcontacto(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  contacto1 = contacto(nombre=informacion["nombre"], apellido=informacion["apellido"], correo= informacion["correo"] )
                  contacto1.save( )
                  return render(request, "App1/regExitoso.html")
      else:
            miFormulario = fcontacto()
 
      return render(request, "App1/formContacto.html", {"miFormulario": miFormulario})

#VISTA FORMULARIOS DE BUSQUEDA
#CARNE
def busquedaCarnes(request):
    return render (request, "App1/busquedaCarnes.html")

def busquedaVerduras(request):
    return render (request, "App1/busquedaVerduras.html")
def busquedaPastas(request):
    return render (request, "App1/busquedaPastas.html")

#VISTA RESULTADOS
#CARNE
def resultadosCarnes(request):
    if request.method == "GET":
        nombre= request.GET["nombre"]
        recetasres= recCarne.objects.filter(nombre__icontains= nombre)
        
        return render (request, "App1/resultadoCarne.html", {"recetas":recetasres, "nombre":nombre })
    else:
        respuesta= "No enviaste datos."
    return HttpResponse(respuesta)
#VERDURAS
def resultadosVerduras(request):
    if request.method == "GET":
        fecha= request.GET["fechaDeSubida"]
        recetasres= recVerduras.objects.filter(fechaDeSubida__icontains= fecha)
        return render (request, "App1/resultadoVerduras.html", {"recetas":recetasres, "fecha":fecha})
    else:
        respuesta= "No enviaste datos."
    return HttpResponse(respuesta)
#PASTAS
def resultadosPastas(request):
    if request.method == "GET":
        nombre= request.GET["nombre"]
        recetasres= recPastas.objects.filter(nombre__icontains= nombre)
        return render (request, "App1/resultadoPastas.html", {"recetas":recetasres, "name":nombre})
    else:
        respuesta= "No enviaste datos."
    return HttpResponse(respuesta)