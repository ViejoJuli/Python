from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from gestionPedidos.models import Articulos
from django.conf import settings #Import setting.py
from django.core.mail import send_mail
from gestionPedidos.forms import ContactForm
# Create your views here. (Always get info from a request!)
def products_search(request):
    return render(request,"products_search.html")

#Function that verifies if info goes to server
def search(request):
    if request.GET['product']:
        product=request.GET['product']
        if len(product)>20:
            message="Searched Item too Long"
        else:  
            items=Articulos.objects.filter(nombre__icontains=product) #icontains=like
            return render(request,"search_results.html",{"items":items,"query":product}) #Creates a render to see information of product
    else:
        message="No Item Searched"
    return HttpResponse(message)

def contact (request):
    if request.method=="POST":
        myform=ContactForm(request.POST)
        if myform.is_valid():
            infform=myform.cleaned_data
            send_mail(infform["subject"],infform["message"],
            infform.get("email",""),["jdrios111@gmail.com"]) #If let it empty(""),anyway it send to email
            return render(request,"thanks.html")
    else:
        myform=ContactForm() #Creates empty form
    return render(request,"contact_form.html",{"form":myform})

    """subject=request.POST["subject"]
        message=request.POST["message"]+" "+request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["jdrios111@gmail.com"] #Where messages arrives
        send_mail(subject,message,email_from,recipient_list)
        return render(request,"thanks.html")
    return render(request,"contact.html")"""