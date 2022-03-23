import json

import requests
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
#from tablib import Dataset
from emi.models import *
from .forms import *
from .resources import *
from tablib import Dataset
from django.core.paginator import Paginator


def creer_horaire(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = BookForm()
    return render(request, 'horaire.html', {
        'form': form
    })
def point(request):
    if request.method == 'POST':
        form = PointForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_home')
    else:
        form = PointForm()
    return render(request, 'point.html', {
        'form': form
    })

def import_etudiant(request):
    classes=Classes.objects.all()
    return render(request, 'import_etudiant.html',{'classes':classes})
def import_etudiant_save(request):
    if request.method == 'POST':
        #classe=Facultes.objects.all()
        person_resource =EtudiantResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']
        #selecte_fac=request.POST.get('fac')
        #fac=Facultes.objects.get(fac_nom=selecte_fac)
        #name=request.POST.get('name')
        #print(selecte_fac)
        imported_data = dataset.load(new_persons.read(),format='xlsx')
        print(imported_data)
        #try:
        for data in imported_data:
            if data[-1]!=None or data[-2]!=None:
                #username=data[0]
                classe_nom=request.POST.get('classe')
                classe_obj=Classes.objects.get(id=classe_nom)
                
                #print(username)
                #profile_pic_url = str(media/username.png)

                user=CustomUser.objects.create_user(username=data[-2],
                    password=data[-1],
                    email=data[-3],
                    last_name=data[2],
                    first_name=data[1],
                    user_type=2)
                user.students.student_roll=data[0]
                user.students.etudiant_prenom= data[3]
                user.students.gender=data[4]
                user.students.etudiant_date_de_naissance=data[5]
                user.students.etudiant_lieu_de_naissance= data[6]
                user.students.etudiant_nationalite= data[7]
                user.students.etudiant_groupe_sanguin=data[8]
                user.students.address=data[9]                
                user.students.select_class=classe_obj
                #user.students.profile_pic=profile_pic_url
                #user.students.profile_pic=profile_pic_url
                user.save()

            #else:
                #break
        ##messages.success(request, "Bien sauvegarder")
        return HttpResponseRedirect(reverse("admin_home"))



def promotion(request):

    departement=Departement.objects.all()
    return render(request,"add_classe.html",{"departement":departement})

def point_(request):
    classe=Classes.objects.all()
    return render(request,"point.html",{"classe":classe})

def promotion_save(request):
    if request.method=='POST':
        semestre_code=request.POST.get('code')
        select_departement=request.POST.get('departement')
        semestre_nom=request.POST.get('nom')
        semestre=Classes(classe_code=semestre_code,classe_nom=semestre_nom)
        departement=Departement.objects.get(id=select_departement)
        semestre.departement_select=departement
        semestre.save()
        ##messages.success(request, "Bien sauvegarder")
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        return HttpResponse("<h2>Method Not Allowed</h2>")

def add_student(request):
    classes=Classes.objects.all()
    return render(request,"add_student_template.html",{'classes':classes})

def add_student_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        prenom=request.POST.get('prenom')
        date=request.POST.get('date')
        lieu=request.POST.get('lieu')
        sang=request.POST.get('sang')
        nationalite=request.POST.get('nationalite')
        #print(faculte_deuxieme)
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        address = request.POST.get("address")
        select_class = request.POST.get("select_class")
        sex = request.POST.get("sex")
        student_roll=request.POST.get('student_roll')
        if request.FILES.get('profile_pic',False):
            profile_pic=request.FILES['profile_pic']
            fs=FileSystemStorage()
            filename=fs.save(profile_pic.name,profile_pic)
            profile_pic_url=fs.url(filename)
        else:
            profile_pic_url=None

    #try:
        user=CustomUser.objects.create_user(password=password,username=username,email=email,last_name=last_name,first_name=first_name,user_type=2)
        user.students.etudiant_prenom= prenom
        user.students.address=address
        user.students.etudiant_groupe_sanguin=sang
        user.students.etudiant_date_de_naissance=date
        user.students.etudiant_lieu_de_naissance= lieu
        user.students.etudiant_nationalite= nationalite
        user.students.student_roll=student_roll
        classe_obj=Classes.objects.get(id=select_class)
        user.students.select_class=classe_obj
        user.students.gender=sex
        if profile_pic_url!=None:
            user.students.profile_pic=profile_pic_url
            #user_obj=Etudiant.objects.filter(etudiant_matri=roll).exists()
        user.save()
        ##messages.success(request, "Bien ajouter")
        return HttpResponseRedirect(reverse("admin_home"))
        #else:
            ##messages.success(request, "profile non reconnu")
            #return HttpResponseRedirect(reverse("add_student"))
    #except:
            ##messages.error(request,"EchecStudent")
            #return HttpResponseRedirect(reverse("add_student"))

def departement(request):
    
    return render(request,"add_departement.html")

def departement_save(request):
	if request.method=='POST':
		titre=request.POST.get('titre')
		status=request.POST.get('status')
		contenu=request.POST.get('texte')
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		
		exist=Departement.objects.filter(titre=titre,contenu=contenu).exists()
		if exist:
		    emi=Departement.objects.get(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    
		    emi.save()
		    ##messages.success(request, "bien ajouter")
		else:
		    emi=Departement(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		
		    emi.save()
		    
		return HttpResponseRedirect(reverse("appercu"))
@login_required
def appercu(request):

    image=ImageAr.objects.all()

    etudiant=Students.objects.all().count()

    fille=Students.objects.filter(gender='Feminin').count()
    garcon=Students.objects.filter(gender='Masculin').count()
    evenement=Departement.objects.all()
    event=Evenements.objects.all()
    project=Projects.objects.all()
    partenaire=Partenaires.objects.all()
    departement=Departement.objects.all().count()
    profile=Profile.objects.all()
    opportunite=Opportunites.objects.all()
    prof=Profs.objects.all()
    emis=Emi.objects.all()
    info=Info.objects.all()
    emi=Articles.objects.all()
    return render(request,'index.html',{"emi":emi,'image':image,'info':info, 'evenement':evenement,'profile':profile,'emis':emis,'departement':departement,'prof':prof,'event':event,'project':project,'opportunite':opportunite,'partenaire':partenaire,'fille':fille,'garcon':garcon,'etudiant':etudiant})
def lire_article(request,id):
    article=Articles.objects.get(id=id)
    all_article=Articles.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,'article_details.html',{'article':article,'all_article':all_article,'evenement':evenement,'partenaire':partenaire})
def lire_project(request,id):
    article=Projects.objects.get(id=id)
    all_article=Projects.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    return render(request,'project_details.html',{'article':article,'all_article':all_article,'evenement':evenement,'partenaire':partenaire})
    
def lire_profile(request,id):

    article=Profile.objects.get(id=id)
    partenaire=Partenaires.objects.filter(status=True)

    all_article=Profile.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    return render(request,'profile_details.html',{'article':article,'all_article':all_article,'evenement':evenement,'partenaire':partenaire})
def contacte(request):
    image=ImageAr.objects.all()
    emi=Emi.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    return render (request,'contact.html',{'image':image,'emi':emi,'partenaire':partenaire})

def lire_departement(request,id):
    article=Departement.objects.get(id=id)
    all_article=Departement.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,'departement_details.html',{'article':article,'all_article':all_article,'evenement':evenement,'partenaire':partenaire})
    
def lire_evenement(request,id):
    article=Evenements.objects.get(id=id)
    all_article=Evenements.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,'evenement_details.html',{'article':article,'all_article':all_article,'evenement':evenement,'partenaire':partenaire})
def lire_opportunite(request,id):
    article=Opportunites.objects.get(id=id)

    all_article=Opportunites.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,'opportunite_details.html',{'article':article,'all_article':all_article,'evenement':evenement,'partenaire':partenaire})
@login_required
def admin_home(request):
    subject_count=Articles.objects.all().count()
    etudiant=Students.objects.all().count()
    classe_count_=Profile.objects.all().count()
    pub=Articles.objects.filter(status=False).count()
    pubs=Articles.objects.filter(status=True).count()
    return render(request,"home_content.html",{"pub":pub, "pubs":pubs, "student_count":classe_count_,"subject_count":subject_count,'etudiant':etudiant})

def add_emi(request):
	return render(request,"emi.html")

def add_profile(request):
	return render(request,"profile.html")

def add_emi_save(request):
	if request.method=='POST':
		#nom=request.POST.get('nom')
		emi_phone=request.POST.get('phone')
		email=request.POST.get('email')
		emi_adresse=request.POST.get('addresse')
		status=request.POST.get('status')
		exist=Emi.objects.filter(status=True).exists()
		if exist:
			emi=Emi.objects.get(status=True)
			emi.emi_phone=emi_phone
			emi.emi_email=email
			emi.emi_adresse=emi_adresse
			emi.save()
		else:
			#if profile_pic_url!=None:
				emi=Emi(emi_adresse=emi_adresse,emi_phone=emi_phone,emi_email=email,status=status)
				emi.save()
		###messages.success(request, "bien ajouter")
		return HttpResponseRedirect(reverse("appercu"))
def apropos_nous(request):
    apropos=Appropos.objects.filter(status=True)
    image=ImageAr.objects.all()
    partenaire=Partenaires.objects.filter(status=True)

    return render (request,'apropos.html',{'image':image,'apropos':apropos,'partenaire':partenaire})

def add_profile_save(request):

	if request.method=='POST':

		nom=request.POST.get('nom')
		postnom=request.POST.get('postnom')
		prenom=request.POST.get('prenom')
		texte=request.POST.get('texte')
		grade=request.POST.get('grade')
		status=request.POST.get('status')
		position=request.POST.get('position')
		if request.FILES.get('profile_pic',False):
			profile_pic=request.FILES['profile_pic']
			fs=FileSystemStorage()
			filename=fs.save(profile_pic.name,profile_pic)
			profile_pic_url=fs.url(filename)
		else:
			profile_pic_url=None
		exist=Profile.objects.filter(prof_nom=nom,prof_prenom=prenom,prof_postnom=postnom).exists()
		if exist:
			emi=Profile.objects.get(prof_nom=nom,prof_prenom=prenom,prof_postnom=postnom)
			emi.grade_ac=grade
			emi.texte=texte
			emi.status=status
			emi.position=position
			if profile_pic_url!=None:
				emi.image=profile_pic_url
			emi.save()
		else:
			if profile_pic_url!=None:
				emi=Profile(prof_nom=nom,prof_prenom=prenom,prof_postnom=postnom,position=position,image=profile_pic_url,status=status,texte=texte,grade_ac=grade)
			emi.save()
		##messages.success(request, "bien ajouter")
		return HttpResponseRedirect(reverse("appercu"))

def creer_image(request):
    return render(request,'image.html')

def creer_horaire_(request):
    return render(request,'horaire.html')

def creer_partenaire(request):
    return render(request,'partenaire.html')

def creer_project(request):
    return render(request,'project.html')

def creer_opportunite(request):
    return render(request,'opportunite.html')

def creer_evenement(request):
    #form=ArticlesForm()
    return render(request,'evenement.html')

def creer_article(request):
    form=ArticlesForm()
    return render(request,'article.html',{'form':form})

def etudiant(request):
    return render (request,'etudiant.html')
def etudiant_save(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        status=request.POST.get('status')
        ece=Info.objects.filter(status=True).exists()
        if ece :
            emi=Info.objects.get(status=True)
            emi.nombre_etudiants=nombre
            emi.save()
        else:
            
            emi=Info(nombre_etudiants=nombre,status=status)
            emi.save()
    return HttpResponseRedirect(reverse("appercu"))

def prof(request):
    return render (request,'prof.html')
def prof_save(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        status=request.POST.get('status')
        ece=Profs.objects.filter(status=True).exists()
        if ece :
            emi=Profs.objects.get(status=True)
            emi.nomb_prof=nombre
            emi.save()
        else:
            
            emi=Profs(nomb_prof=nombre,status=status)
            emi.save()
    return HttpResponseRedirect(reverse("appercu"))

def delete_partenaire(request,id):

    profile=Partenaires.objects.get(id=id)

    try:
        profile.delete()
        return redirect('appercu')
    except:
        return redirect('appercu')
def liste_etudiant(request):
    students=Students.objects.all()
    return render(request,'manage_student_template.html',{'students':students})

def delete_article(request,id):
    profile=Articles.objects.get(id=id)
    try:
        profile.delete()
        return redirect('appercu')
    except:
        return redirect('appercu')
def delete_student(request,id):
    profile=Students.objects.get(admin=id)
    try:
        profile.delete()
        return redirect('liste_etudiant')
    except:
        return redirect('liste_etudiant')

def delete_departement(request,id):
    profile=Departement.objects.get(id=id)
    try:
        profile.delete()
        return redirect('appercu')
    except:
        return redirect('appercu')

def delete_evenement(request,id):
    profile=Evenements.objects.get(id=id)
    try:
        profile.delete()
        return redirect('appercu')
    except:
        return redirect('appercu')

def delete_project(request,id):

    profile=Projects.objects.get(id=id)

    try:
        profile.delete()
        return redirect('appercu')
    except:
        return redirect('appercu')

def delete_opportunite(request,id):
    profile=Opportunites.objects.get(id=id)
    try:
        profile.delete()
        return redirect('appercu')
    except:
        return redirect('appercu')
    
def delete_profile(request, profile_id):
    staff =Profile.objects.get(id=profile_id)
    try:
        staff.delete()
        ##messages.success(request, "Effacer.")
        return redirect('appercu')
    except:
        ##messages.error(request, "Echec.")
        return redirect('appercu')

def admin_profile(request):
    user=CustomUser.objects.get(id=request.user.id)
    return render(request,"admin_profile.html",{"user":user})

def admin_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("admin_profile"))
    else:
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            customuser=CustomUser.objects.get(adminhod=request.user.id)
            customuser.first_name=first_name
            customuser.last_name=last_name
            if password!=None and password!="":
                customuser.set_password(password)
            customuser.save()
            ##messages.success(request, "modification ajouter")
            return HttpResponseRedirect(reverse("appercu"))
        except:
            ##messages.error(request, "Echec")
            return HttpResponseRedirect(reverse("appercu"))
def prevu_emi(request):
	emi=Emi.objects.all()
	return render(request,'emi_vu.html',{'emi':emi})
def prevu_article(request):

	emi=Articles.objects.all()

	return render(request,'article_vu.html',{'emi':emi})

def creer_article_save(request):
	if request.method=='POST':
		titre=request.POST.get('titre')
		status=request.POST.get('status')
		contenu=request.POST.get('texte')
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		print(profile_pic_url)
		exist=Articles.objects.filter(titre=titre,contenu=contenu).exists()
		if exist:
		    emi=Articles.objects.get(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    
		    emi.save()
		    ##messages.success(request, "bien ajouter")
		else:
		    emi=Articles(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		
		    emi.save()
		    
		return HttpResponseRedirect(reverse("appercu"))
def creer_image_save(request):
	if request.method=='POST':
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		status=request.POST.get('status')
		exist=ImageAr.objects.filter(status=status).exists()
		
		if exist:
		    emi=ImageAr.objects.get(status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		else:
		    emi=ImageAr(status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		    
		return HttpResponseRedirect(reverse("appercu"))
def point_save(request):
	if request.method=='POST':
		clas=request.POST.get('classe')
		print(request.FILES.get('profile_pic'))
		classe=Classes.objects.get(id=clas)
		status=request.POST.get('status')
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		#print(profile_pic_url)
		exist=Points.objects.filter(status=status,classe=classe).exists()
		
		if exist:
		    emi=Points.objects.get(status=status,classe=classe)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		else:
		    emi=Points(status=status,classe=classe)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		    
		return HttpResponseRedirect(reverse("admin_home"))
def creer_horaire_save(request):

	if request.method=='POST':
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		print(profile_pic_url)
		status=request.POST.get('status')
		exist=Horaire.objects.filter(status=status).exists()
		
		if exist:
		    emi=Horaire.objects.get(status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		else:
		    emi=Horaire(status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		   
		return HttpResponseRedirect(reverse("admin_home"))


def creer_partenaire_save(request):
	if request.method=='POST':
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		status=request.POST.get('status')
		emi=Partenaires(status=status)
		if profile_pic_url!=None:
		    emi.photo=profile_pic_url
		emi.save()
		return HttpResponseRedirect(reverse("appercu"))

def creer_evenement_save(request):
	if request.method=='POST':
		titre=request.POST.get('titre')
		lieu=request.POST.get('lieu')
		status=request.POST.get('status')
		contenu=request.POST.get('texte')
		jour=request.POST.get('jour')
		mois=request.POST.get('mois')
		heure=request.POST.get('heure')
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		if request.FILES.get('video',False):
		    profile_pic=request.FILES['video']

		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    video_url=fs.url(filename)
		else:
		    video_url=None
		exist=Evenements.objects.filter(titre=titre,contenu=contenu).exists()
		if exist:
		    emi=Evenements.objects.get(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    if video_url!=None:
		        emi.video=video_url
		    emi.save()
		       
		    #messages.success(request, "bien ajouter")
		else:
		    emi=Evenements(titre=titre,contenu=contenu,status=status,heure=heure,jour=jour,mois=mois,lieu=lieu)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    if video_url!=None:
		        emi.video=video_url
		    emi.save()
		    
		return HttpResponseRedirect(reverse("appercu"))


def creer_project_save(request):
	if request.method=='POST':
		titre=request.POST.get('titre')
		#date=request.POST.get('date')
		status=request.POST.get('status')
		contenu=request.POST.get('texte')
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		exist=Projects.objects.filter(titre=titre,contenu=contenu).exists()
		if exist:
		    emi=Projects.objects.get(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		        emi.save()
		        #messages.success(request, "bien ajouter")
		else:
		    emi=Projects(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		    
		return HttpResponseRedirect(reverse("appercu"))

def creer_opportunite_save(request):
	if request.method=='POST':
		titre=request.POST.get('titre')
		#date=request.POST.get('date')
		status=request.POST.get('status')
		contenu=request.POST.get('texte')
		if request.FILES.get('profile_pic',False):
		    profile_pic=request.FILES['profile_pic']
		    fs=FileSystemStorage()
		    filename=fs.save(profile_pic.name,profile_pic)
		    profile_pic_url=fs.url(filename)
		else:
		    profile_pic_url=None
		print(profile_pic_url)
		exist=Opportunites.objects.filter(titre=titre,contenu=contenu).exists()
		if exist:
		    emi=Opportunites.objects.get(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		        emi.save()
		        #messages.success(request, "bien ajouter")
		else:
		    emi=Opportunites(titre=titre,contenu=contenu,status=status)
		    if profile_pic_url!=None:
		        emi.photo=profile_pic_url
		    emi.save()
		    
		return HttpResponseRedirect(reverse("appercu"))

def update_departement(request,id):
    request.session['id']=id
    student=Departement.objects.get(id=id)
    form=DepartementForm()
    form.fields['titre'].initial=student.titre
    form.fields['contenu'].initial=student.contenu
    form.fields['status'].initial=student.status
    return render(request,"update_departement.html",{"form":form,"id":id})

def update_departement_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        id=request.session.get("id")
        if id==None:
            return HttpResponseRedirect(reverse("appercu"))

        form=DepartementForm(request.POST,request.FILES)
        if form.is_valid():
            titre= form.cleaned_data['titre']
            contenu= form.cleaned_data["contenu"]
            
            status = form.cleaned_data["status"]

            if request.FILES.get('photo',False):
                profile_pic=request.FILES['photo']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            #try:
            user=Departement.objects.get(id=id)
            user.titre=titre
            user.contenu=contenu
            user.status=status
            if profile_pic_url!=None:
                user.photo=profile_pic_url
            user.save()
            del request.session['id']
            #messages.success(request,"modification ajouter ")
            return HttpResponseRedirect(reverse("appercu"))
            #except:
                ##messages.error(request,"Echec de modification")
            #return HttpResponseRedirect(reverse("appercu"))
        else:
            form=DepartementForm(request.POST)
            student=Departement.objects.get(id=id)
            return render(request,"update_departement.html",{"form":form,"id":id})

def update_article(request,id):

    request.session['id']=id

    student=Articles.objects.get(id=id)
    form=ArticlesForm()
    form.fields['titre'].initial=student.titre
    form.fields['contenu'].initial=student.contenu
    form.fields['status'].initial=student.status
    return render(request,"update_article.html",{"form":form,"id":id})

def update_article_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        id=request.session.get("id")
        if id==None:
            return HttpResponseRedirect(reverse("appercu"))

        form=ArticlesForm(request.POST,request.FILES)
        if form.is_valid():
            titre= form.cleaned_data['titre']
            contenu= form.cleaned_data["contenu"]
            
            status = form.cleaned_data["status"]

            if request.FILES.get('photo',False):
                profile_pic=request.FILES['photo']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            #try:
            user=Articles.objects.get(id=id)
            user.titre=titre
            user.contenu=contenu
            user.status=status
            if profile_pic_url!=None:
                user.photo=profile_pic_url
            user.save()
            del request.session['id']
            #messages.success(request,"modification ajouter ")
            return HttpResponseRedirect(reverse("appercu"))
            #except:
                ##messages.error(request,"Echec de modification")
            #return HttpResponseRedirect(reverse("appercu"))
        else:
            form=ArticlesForm(request.POST)
            student=Articles.objects.get(id=id)
            return render(request,"update_article.html",{"form":form,"id":id})

def update_opportunite(request,id):

    request.session['id']=id

    student=Opportunites.objects.get(id=id)
    form=OpportuniteForm()
    form.fields['titre'].initial=student.titre
    form.fields['contenu'].initial=student.contenu
    form.fields['status'].initial=student.status
    return render(request,"update_opportunite.html",{"form":form,"id":id})

def update_opportunite_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        id=request.session.get("id")
        if id==None:
            return HttpResponseRedirect(reverse("appercu"))

        form=OpportuniteForm(request.POST,request.FILES)
        if form.is_valid():
            titre= form.cleaned_data['titre']
            contenu= form.cleaned_data["contenu"]
            
            status = form.cleaned_data["status"]

            if request.FILES.get('photo',False):
                profile_pic=request.FILES['photo']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            #try:
            user=Opportunites.objects.get(id=id)
            user.titre=titre
            user.contenu=contenu
            user.status=status
            if profile_pic_url!=None:
                user.photo=profile_pic_url
            user.save()
            del request.session['id']
            #messages.success(request,"modification ajouter ")
            return HttpResponseRedirect(reverse("appercu"))
            #except:
                ##messages.error(request,"Echec de modification")
            #return HttpResponseRedirect(reverse("appercu"))
        else:
            form=OpportuniteForm(request.POST)
            student=Opportunites.objects.get(id=id)
            return render(request,"update_opportunite.html",{"form":form,"id":id})



def update_project(request,id):
    request.session['id']=id
    student=Projects.objects.get(id=id)
    form=ProjectForm()
    form.fields['titre'].initial=student.titre
    form.fields['contenu'].initial=student.contenu
    form.fields['status'].initial=student.status
    return render(request,"update_project.html",{"form":form,"id":id})

def update_project_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        id=request.session.get("id")
        if id==None:
            return HttpResponseRedirect(reverse("appercu"))

        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            titre= form.cleaned_data['titre']
            contenu= form.cleaned_data["contenu"]
            
            status = form.cleaned_data["status"]

            if request.FILES.get('photo',False):
                profile_pic=request.FILES['photo']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            #try:
            user=Projects.objects.get(id=id)
            user.titre=titre
            user.contenu=contenu
            user.status=status
            if profile_pic_url!=None:
                user.photo=profile_pic_url
            user.save()
            del request.session['id']
            #messages.success(request,"modification ajouter ")
            return HttpResponseRedirect(reverse("appercu"))
            #except:
                ##messages.error(request,"Echec de modification")
            #return HttpResponseRedirect(reverse("appercu"))
        else:
            form=ProjectForm(request.POST)
            student=Projects.objects.get(id=id)
            return render(request,"update_project.html",{"form":form,"id":id})


def edite_profile(request,id):

    request.session['id']=id

    student=Profile.objects.get(id=id)
    form=ProfilesForm()
    form.fields['prof_prenom'].initial=student.prof_prenom
    form.fields['prof_nom'].initial=student.prof_nom
    form.fields['prof_postnom'].initial=student.prof_postnom
    form.fields['grade_ac'].initial=student.grade_ac
    form.fields['texte'].initial=student.texte
    form.fields['position'].initial=student.position
    form.fields['status'].initial=student.status
    return render(request,"update_profile.html",{"form":form,"id":id})

def edite_profile_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        id=request.session.get("id")
        if id==None:
            return HttpResponseRedirect(reverse("appercu"))

        form=ProfilesForm(request.POST,request.FILES)
        if form.is_valid():
            prof_prenom= form.cleaned_data['prof_prenom']
            prof_nom= form.cleaned_data['prof_nom']
            prof_postnom= form.cleaned_data['prof_postnom']
            grade_ac= form.cleaned_data['grade_ac']
            texte= form.cleaned_data["texte"]
            position= form.cleaned_data["position"]
            
            status = form.cleaned_data["status"]

            if request.FILES.get('image',False):
                profile_pic=request.FILES['image']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None


            try:
                user=Profile.objects.get(id=id)
                user.prof_prenom=prof_prenom
                user.prof_nom=prof_nom
                user.prof_postnom=prof_postnom
                user.grade_ac=grade_ac
                user.texte=texte
                user.position=position
                user.status=status
                if profile_pic_url!=None:
                    user.image=profile_pic_url
                user.save()
                del request.session['id']
                ##messages.success(request,"modification ajouter ")
                return HttpResponseRedirect(reverse("appercu"))
            except:
                #messages.error(request,"Echec de modification")
                return HttpResponseRedirect(reverse("appercu"))
        else:
            form=ProfileForm(request.POST)
            student=Profile.objects.get(id=id)
            return render(request,"update_profile.html",{"form":form,"id":id})



def update_evenement(request,id):
    request.session['id']=id
    student=Evenements.objects.get(id=id)
    form=EvenementForm()
    form.fields['titre'].initial=student.titre
    form.fields['contenu'].initial=student.contenu
    form.fields['jour'].initial=student.jour

    form.fields['mois'].initial=student.mois
    form.fields['lieu'].initial=student.lieu
    form.fields['heure'].initial=student.heure
    
    form.fields['status'].initial=student.status
    return render(request,"update_evenement.html",{"form":form,"id":id})

def update_evenement_save(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        id=request.session.get("id")
        if id==None:
            return HttpResponseRedirect(reverse("appercu"))

        form=EvenementForm(request.POST,request.FILES)
        if form.is_valid():
            titre= form.cleaned_data['titre']
            jour= form.cleaned_data['jour']
            mois= form.cleaned_data['mois']
            lieu= form.cleaned_data['lieu']
            heure= form.cleaned_data['heure']
            contenu= form.cleaned_data["contenu"]
            
            status = form.cleaned_data["status"]

            if request.FILES.get('photo',False):
                profile_pic=request.FILES['photo']
                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                profile_pic_url=fs.url(filename)
            else:
                profile_pic_url=None
            if request.FILES.get('video',False):

                profile_pic=request.FILES['video']

                fs=FileSystemStorage()
                filename=fs.save(profile_pic.name,profile_pic)
                video_url=fs.url(filename)
            else:
                video_url=None



            try:
                user=Evenements.objects.get(id=id)
                user.titre=titre
                user.jour=jour
                user.mois=mois
                user.heure=heure
                user.lieu=lieu
                user.contenu=contenu
                user.status=status
                if profile_pic_url!=None:
                    user.photo=profile_pic_url
                if video_url!=None:
                    user.video=video_url
                user.save()
                del request.session['id']
                ##messages.success(request,"modification ajouter ")
                return HttpResponseRedirect(reverse("appercu"))
            except:
                ##messages.error(request,"Echec de modification")
                return HttpResponseRedirect(reverse("appercu"))
        else:
            form=EvenementForm(request.POST)
            student=Evenements.objects.get(id=id)
            return render(request,"update_evenement.html",{"form":form,"id":id})


def appropos(request):

    return render (request,'appropos.html')

def appropos_save(request):
    if request.method=='POST':
        nombre=request.POST.get('texte')
        status=request.POST.get('status')
        ece=Appropos.objects.filter(status=True).exists()
        if ece :
            emi=Appropos.objects.get(status=True)
            emi.appropos=nombre
            emi.save()
        else:
            
            emi=Appropos(appropos=nombre,status=status)
            emi.save()
    return HttpResponseRedirect(reverse("appercu"))
def all_articles(request):
    image=ImageAr.objects.filter(status=True)
    evenement=Departement.objects.filter(status=True)
    article=Articles.objects.order_by('-id').filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    paginator=Paginator(article,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,"all_articles.html",{'article':page_object, 'evenement':evenement,'partenaire':partenaire})
def all_evenements(request):
    article=Evenements.objects.order_by('-id').filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    paginator=Paginator(article,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,"all_evenements.html",{'article':page_object, 'evenement':evenement,'partenaire':partenaire})
def all_departements(request):
    article=Departement.objects.order_by('-id').filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    paginator=Paginator(article,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,"all_departements.html",{'article':page_object, 'evenement':evenement,'partenaire':partenaire})
def all_opportunites(request):
    article=Opportunites.objects.order_by('-id').filter(status=True)
    evenement=Departement.objects.filter(status=True)
    paginator=Paginator(article,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,"all_opportunites.html",{'article':page_object, 'evenement':evenement,'partenaire':partenaire})
def all_profiles(request):
    article=Profile.objects.order_by('-id').filter(status=True)
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    paginator=Paginator(article,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,"all_profiles.html",{'article':page_object, 'evenement':evenement,'partenaire':partenaire})
def all_projects(request):
    evenement=Departement.objects.filter(status=True)
    partenaire=Partenaires.objects.filter(status=True)
    article=Projects.objects.order_by('-id').filter(status=True)
    paginator=Paginator(article,2)
    page_number=request.GET.get('page')
    page_object=paginator.get_page(page_number)
    partenaire=Partenaires.objects.filter(status=True)
    return render(request,"all_projects.html",{'article':page_object, 'evenement':evenement,'partenaire':partenaire})