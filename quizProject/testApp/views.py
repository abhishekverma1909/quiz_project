from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testApp.forms import SignUpForm
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from testApp.models import Javamcq,Pythonmcq,Cplusmcq,Aptitudemcq
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import datetime


# Create your views here.
def home_view(request):
    return render(request,'testApp/home.html')

def lhome_view(request):
    return render(request,'testApp/lhome.html')



def Phome_view(request):
    return render(request,'testApp/Phome.html')
def Chome_view(request):
    return render(request,'testApp/Chome.html')
def Jhome_view(request):
    return render(request,'testApp/Jhome.html')
def Ahome_view(request):
    return render(request,'testApp/Ahome.html')



def logout_view(request):
    return render(request,'testApp/logout.html')

@login_required
def java_view(request):
    global time1
    time1=datetime.datetime.now()
    mcq=Javamcq.objects.all()
    paginator=Paginator(mcq,1)
    page_number=request.GET.get('page')
    try:
        mcq=paginator.page(page_number)
    except PageNotAnInteger:
        mcq=paginator.page(1)
    except EmptyPage:
        mcq=paginator.page(page.num_pages)
    return render(request,'testApp/javaexam.html',{'mcq':mcq,'time1':time1})



@login_required
def python_view(request):
    global time1
    time1=datetime.datetime.now()
    mcq=Pythonmcq.objects.all()
    paginator=Paginator(mcq,1)
    page_number=request.GET.get('page')
    try:
        mcq=paginator.page(page_number)
    except PageNotAnInteger:
        mcq=paginator.page(1)
    except EmptyPage:
        mcq=paginator.page(page.num_pages)

    return render(request,'testApp/pythonexam.html',{'mcq':mcq,'time1':time1})


def result_view(request):
    time2=datetime.datetime.now()
    return render(request, 'testApp/result.html',{'time':time2-time1})



@login_required
def c_view(request):
    global time1
    time1=datetime.datetime.now()
    mcq=Cplusmcq.objects.all()
    paginator=Paginator(mcq,1)
    page_number=request.GET.get('page')
    try:
        mcq=paginator.page(page_number)
    except PageNotAnInteger:
        mcq=paginator.page(1)
    except EmptyPage:
        mcq=paginator.page(page.num_pages)
    return render(request,'testApp/c++exam.html',{'mcq':mcq,'time1':time1})

@login_required
def aptitude_view(request):
    global time1
    time1=datetime.datetime.now()
    mcq=Aptitudemcq.objects.all()
    paginator=Paginator(mcq,1)
    page_number=request.GET.get('page')
    try:
        mcq=paginator.page(page_number)
    except PageNotAnInteger:
        mcq=paginator.page(1)
    except EmptyPage:
        mcq=paginator.page(page.num_pages)
    return render(request,'testApp/aptitudeexam.html',{'mcq':mcq,'time1':time1})





def SignUpForm_View(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testApp/signup.html',{'form':form})
