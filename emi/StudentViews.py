import datetime

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from emi.models import *

@login_required
def student_home(request):
    student_obj=Students.objects.get(admin=request.user.id)
    classe=Classes.objects.get(id=student_obj.select_class.id)
    horaire=Horaire.objects.filter(status=True)
    horaires=Horaire.objects.all().count()
    student_obj=Students.objects.get(admin=request.user.id)
    cla=Classes.objects.get(id=student_obj.select_class.id)
    point=Points.objects.filter(classe=cla)
    points=Points.objects.filter(classe=cla).count()
    return render(request,"student_template/student_home_template.html",{'users':student_obj,'classe':classe,'horaire':horaire,'horaires':horaires,"point":point,'points':points})
def telecharge_horaire(request):
    horaire=Horaire.objects.filter(status=False)
    return render(request,"student_template/horaire.html",{'horaire':horaire,})
def telecharge_valve(request):
    student_obj=Students.objects.get(admin=request.user.id)
    cla=Classes.objects.get(id=student_obj.select_class.id)
    point=Points.objects.filter(classe=cla)
    return render(request,"student_template/point.html",{'point':point})
def student_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    student=Students.objects.get(admin=user)
    return render(request,"student_template/student_profile.html",{"user":user,"student":student})

def student_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("student_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        email=request.POST.get("email")
        address=request.POST.get("address")
        try:
            customuser=CustomUser.objects.get(id=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            customuser.email=email
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()

            student=Students.objects.get(admin=customuser)
            student.address=address
            student.save()
            #messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("student_profile"))
        except:
            #messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("student_profile"))
