from django.shortcuts import render
from django.views.decorators.csrf import requires_csrf_token
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage (/)")
    context={'name':'Pratyush','course':'Django','sir':'CodewithHarry'}
    return render(request,"home.html",context)

def about(request):
    #return HttpResponse("This is my about page (/about)")
    return render(request,"about.html")

def projects(request):
    #return HttpResponse("This is my projects page (/projects)")
    return render(request,"projects.html")

@requires_csrf_token
def contact(request):
    context={'success':False}
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        feedback = request.POST['feedback']
        contact = Contact(name=name,email=email,feedback=feedback) 
        contact.save()
        context={'success':True}
    #return HttpResponse("This is my contact page (/contact)")
    return render(request,"contact.html",context)  
    