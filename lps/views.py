from django.shortcuts import render
from django.db import transaction
from lps.models import FreeConsultationModel
from lps.forms import FreeConsultForm
from django.contrib import messages
from django.core.mail import EmailMessage

from django.http import HttpResponse
# Create your views here.
def hello(request):
    return  render(request,'index.html')

#def about(request):
 #   return render(request, 'about.html')

def contact(request):
    if request.method=="POST":
        errorflag =True
        uname=request.POST.get("username")
        if(len(uname)>32):
            messages.error(request, 'Invalid Name')
            errorflag=False
        mobile=request.POST.get("usermobile")
        if(len(mobile)>10):
            messages.error(request, 'Invalid Mobile number')
            errorflag=False

        email=request.POST.get("useremail")
        subject=request.POST.get("usersubject")
        content=request.POST.get("usercontent")
        #consultation=FreeConsultationModel(name = uname,mob=mobile,email=email,sub=subject,cont=content)
        if(errorflag):
            consultation=FreeConsultationModel(name = uname,cmobilenumber=mobile,cemail=email,subject=subject,message=content,isContacted='False')
            consultation.save()
            messages.success(request, 'Form submission successful')
        return render(request, 'contact.html')
    return render(request, 'contact.html')


def services(request):
    if(request.method == "POST"):
        errorflag = True
        uname = request.POST.get("username")
        if (len(uname) > 32):
            messages.error(request, 'Invalid Name')
            errorflag = False
        mobile = request.POST.get("usermobile")
        if (len(mobile) > 10):
            messages.error(request, 'Invalid Mobile number')
            errorflag = False

        email = request.POST.get("useremail")
        subject = request.POST.get("usersubject")
        content = request.POST.get("usercontent")
        # consultation=FreeConsultationModel(name = uname,mob=mobile,email=email,sub=subject,cont=content)
        if (errorflag):
            consultation = FreeConsultationModel(name=uname, cmobilenumber=mobile, cemail=email, subject=subject,
                                                 message=content, iscontacted='False')
            consultation.save()
            messages.success(request, 'Form submission successful')
        return render(request, 'services.html')


    return render(request, 'services.html')

def about(request):
    #email = EmailMessage('Hello', 'World', to=['mr.sathish.c@gmail.com'])
    #email.send()
    if request.method=="POST":
        errorflag =True
        uname=request.POST.get("username")

        if(len(uname)>32):
            messages.error(request, 'Invalid Name')
            errorflag=False
        mobile=request.POST.get("usermobile")
        if(len(mobile)>10):
            messages.error(request, 'Invalid Mobile number')
            errorflag=False

        email=request.POST.get("useremail")
        subject=request.POST.get("usersubject")
        content=request.POST.get("usercontent")
        #consultation=FreeConsultationModel(name = uname,mob=mobile,email=email,sub=subject,cont=content)
        if(errorflag):
            consultation=FreeConsultationModel(name = uname,cmobilenumber=mobile,cemail=email,subject=subject,message=content,isContacted='False')
            consultation.save()
            messages.success(request, 'Form submission successful')
        return render(request, 'about.html')
    return render(request, 'about.html')

def index(request):
    if request.method=="POST":
        errorflag =True
        uname=request.POST.get("username")
        if(len(uname)>32):
            messages.error(request, 'Invalid Name')
            errorflag=False
        mobile=request.POST.get("usermobile")
        if(len(mobile)>10):
            messages.error(request, 'Invalid Mobile number')
            errorflag=False

        email=request.POST.get("useremail")
        subject=request.POST.get("usersubject")
        content=request.POST.get("usercontent")
        #consultation=FreeConsultationModel(name = uname,mob=mobile,email=email,sub=subject,cont=content)
        if(errorflag):
            consultation=FreeConsultationModel(name = uname,cmobilenumber=mobile,cemail=email,subject=subject,message=content,iscontacted='False')
            consultation.save()
            messages.success(request, 'Form submission successful')
        return render(request, 'index.html')
    return render(request, 'index.html')



