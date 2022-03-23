import datetime
import json
import os

import requests
from django.urls import reverse_lazy,reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from emi.EmailBackEnd import EmailBackEnd
from ecole_des_mines import settings
from emi.forms import *
from django.core import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from emi.models import * 

def acceuil(request):
    image=ImageAr.objects.filter(status=True)
    etudiant=Students.objects.all().count()
    fille=Students.objects.filter(gender='Feminin').count()
    garcon=Students.objects.filter(gender='Masculin').count()
    evenement=Departement.objects.filter(status=True)
    event=Evenements.objects.filter(status=True)
    project=Projects.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    departement=Departement.objects.filter(status=True).count()
    profile=Profile.objects.filter(status=True)
    opportunite=Opportunites.objects.filter(status=True)
    prof=Profs.objects.filter(status=True)
    emis=Emi.objects.filter(status=True)
    info=Info.objects.filter(status=True)
    emi=Articles.objects.filter(status=True)
    return render(request,'uob/index.html',{"emi":emi,'image':image,'info':info, 'evenement':evenement,'profile':profile,'emis':emis,'departement':departement,'prof':prof,'event':event,'project':project,'opportunite':opportunite,'partenaire':partenaire,'fille':fille,'garcon':garcon,'etudiant':etudiant})
def ShowLoginPage(request):
    return render(request,"login_page.html")

def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        '''
        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6LeWtqUZAAAAANlv3se4uw5WAg-p0X61CJjHPxKT"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(url=cap_url,data=cap_data)
        cap_json=json.loads(cap_server_response.text)

        if cap_json['success']==False:
            messages.error(request,"Invalid Captcha Try Again")
            return HttpResponseRedirect("/")
        '''
        user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            if user.user_type=="1":
                return HttpResponseRedirect('/admin_home')
            elif user.user_type=="2":
                return HttpResponseRedirect(reverse("student_home"))
        else:
            messages.error(request,"mot de passe ou username incorrect")
            return HttpResponseRedirect("show_login")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("show_login")
def signup_admin(request):
    return render(request,"signup_admin_page.html")

def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/7.14.6/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "YOUR_API_KEY",' \
         '        authDomain: "FIREBASE_AUTH_URL",' \
         '        databaseURL: "FIREBASE_DATABASE_URL",' \
         '        projectId: "FIREBASE_PROJECT_ID",' \
         '        storageBucket: "FIREBASE_STORAGE_BUCKET_URL",' \
         '        messagingSenderId: "FIREBASE_SENDER_ID",' \
         '        appId: "FIREBASE_APP_ID",' \
         '        measurementId: "FIREBASE_MEASUREMENT_ID"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")