
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact

from datetime import datetime
from django.contrib import messages

def index(request):
    
    return render(request,'index.html')
   # return HttpResponse("this is a homepage")
def about(request):
    return render(request,'about.html')
   # return HttpResponse("this is a about page")
def services(request):
    return render(request,'services.html')
def contact(request):
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = request.POST.get('image')
        desc = data.get('desc')
        contact = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
        return redirect('/contact')
    queryset = Contact.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    context = {'contacts': queryset}
    return render(request,'contact.html',context)
def update_receipe(request, id):
    queryset = Contact.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = request.POST.get('image')
        desc = data.get('desc')
        queryset.name = name
        queryset.desc = desc
        queryset.email = email
        if phone:
            queryset.phone = phone
            queryset.save()
        return redirect('/contact')
    context = {'contacts': queryset}
    return render(request,'update_receipe.html',context)
def delete_receipe(request, id):
    queryset = Contact.objects.get(id = id)
    queryset.delete()
    return redirect('/contact')
    
# Create your views here.
