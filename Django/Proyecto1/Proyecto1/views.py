from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): #receive a request as parameter

    p1=Persona("Julian","Rios")
    lista=["Primero","Segundo","Tercero","Cuarto"]
    #nombre="Juan"
    #apellido="Diaz"
    ahora=datetime.datetime.now()
    #doc_externo=open("C:/Users/Julián Ríos/Desktop/ProyectoDjango/Proyecto1/Proyecto1/Plantillas/miplantilla.html") #Introduce plantilla html
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=loader.get_template("miplantilla.html") #Load templates with loader
    #ctx=Context({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":lista}) #Recibe diccionarios
    #texto=plt.render(ctx) #Recibe un contexto
    #texto=doc_externo.render({"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":lista}) #Recibe un diccionario como contexto
    #return HttpResponse(texto) #Use when loader
    return render(request,"miplantilla.html",{"nombre_persona":p1.nombre,"apellido_persona":p1.apellido,"momento_actual":ahora,"temas":lista})#En settings debe estar el path

def herencia(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"herencia.html",{"dameFecha":fecha_actual})
    
def dar_Fecha(request):
    fecha_actual=datetime.datetime.now()
    texto="""<html>
    <body>
    <h1>
    Fecha y hora actuales %s 
    </h1>
    </body>
    </html>"""%fecha_actual
    return HttpResponse(texto)

def calcular_Edad(request,agno,edad):
    periodo=agno-2022
    edadFutura= edad+periodo
    texto="<html><body><h1>En el año %s tendre %s"%(agno,edadFutura)
    return HttpResponse(texto)
