from django.shortcuts import render
from LoginApp.models import Registration
from django.http import HttpResponse


def RegForm(request):
    return render(request,'registration.html')
def Register(request):
    if request.method=='POST':
        reg=Registration()
        reg.firstname=request.POST.get('fname')
        reg.lastname=request.POST.get('lname')
        reg.address=request.POST.get('address')
        reg.email=request.POST.get('email')
        if request.POST.get('pass')==request.POST.get('cpass'):
            reg.password=request.POST.get('pass')
            reg.cpassword=request.POST.get('cpass')
            reg.save()
            return render(request,'login.html')
        return render(request,'registration.html')
    return HttpResponse('<h1>errors..</h1>')
def Login(request):
    if request.method=='POST':
        mail=request.POST.get('email')
        pass1=request.POST.get('pass')
        if Registration.objects.filter(email=mail,password=pass1):
            return render(request,'homepage.html')
        else:
            return HttpResponse('<h1>not found</h1>')
    return HttpResponse('<h1>errors..</h1>')
