from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from datetime import date
#from PIL import Image

class Emi(models.Model):
    id=models.AutoField(primary_key=True)
    #emi_nom=models.CharField(max_length=1000)
    emi_phone=models.CharField(max_length=254,blank=True,null=True)
    emi_email=models.EmailField(blank=True,null=True)
    emi_adresse=models.CharField(max_length=254)
    #emi_logo=models.FileField(upload_to='emi/logo',blank=True,null=True)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,)
    updated_at=models.DateTimeField(auto_now_add=True,)
    objects=models.Manager()

class Articles(models.Model):
    id=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100)
    contenu=models.TextField()
    #fichier=models.FileField(upload_to='article/',blank=True,null=True)
    photo=models.FileField(upload_to='article/photo',blank=True,null=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.titre

class ImageAr(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.FileField(upload_to='arriereplan/photo',blank=True,null=True)
    status=models.BooleanField(default=False)
class Horaire(models.Model):
    id=models.AutoField(primary_key=True)
    fichier=models.FileField(blank=True,null=True)

    status=models.BooleanField(default=False)
class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(2,"Student"))
    user_type=models.CharField(default=1,max_length=100,choices=user_type_data)
    status=models.BooleanField(default=False)
class Info(models.Model):
    nombre_etudiants=models.CharField(max_length=10485760,null=True,blank=True)
    status=models.BooleanField(default=False)
    
class Profs(models.Model):
    nomb_prof=models.CharField(max_length=10485760,null=True,blank=True)
    #info=models.CharField(max_length=1000000000,null=True,blank=True)
    status=models.BooleanField(default=False)
class Appropos(models.Model):
    appropos=models.TextField()
    status=models.BooleanField(default=False)
#personne pouvant se connecter 
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Profile(models.Model):
    id=models.AutoField(primary_key=True)
    prof_prenom=models.CharField(max_length=1000)
    prof_nom=models.CharField(max_length=1000)
    prof_postnom=models.CharField(max_length=1000)
    texte=models.TextField()
    grade_ac=models.CharField(max_length=1000)
    #fonction=models.CharField(max_length=1000,null=True,blank=True)
    image =models.FileField(upload_to='evenements/photo/',blank=True,null=True)
    status=models.BooleanField(default=False)
    position=models.CharField(max_length=10000, null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False)
    objects=models.Manager()

      
class Evenements(models.Model):
    id=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100)
    contenu=models.TextField()
    photo=models.FileField(upload_to='evenements/photo',blank=True,null=True)
    video=models.FileField(upload_to='evenements/photo',blank=True,null=True)
    status=models.BooleanField(default=False)
    jour=models.CharField(max_length=10000,null=True,blank=True)
    mois=models.CharField(max_length=10000,null=True,blank=True)
    heure=models.CharField(max_length=10000,null=True,blank=True)
    lieu=models.CharField(max_length=10000,null=True,blank=True)
    def __str__(self):
        return self.titre

class Projects(models.Model):
    id=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100)

    contenu=models.TextField()
    photo=models.FileField(upload_to='evenements/photo',blank=True,null=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.titre


class Partenaires(models.Model):
    id=models.AutoField(primary_key=True)
    photo=models.FileField(upload_to='evenements/photo',blank=True,null=True)
    status=models.BooleanField(default=False)
class Opportunites(models.Model):
    id=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100)
    contenu=models.TextField()
    photo=models.FileField(upload_to='evenements/photo/',blank=True,null=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.titre
class Departement(models.Model):
    id=models.AutoField(primary_key=True)
    titre=models.CharField(max_length=100)
    contenu=models.TextField()
    photo=models.FileField(upload_to='evenements/photo/',blank=True,null=True)
    status=models.BooleanField(default=False)
    def __str__(self):
        return self.titre

class Classes(models.Model):
    id=models.AutoField(primary_key=True)
    classe_nom=models.CharField(max_length=1000)
    classe_code=models.CharField(max_length=1000,null=True,blank=True)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True,)
    updated_at=models.DateTimeField(auto_now_add=True,)
    departement_select=models.ForeignKey(Departement,on_delete=models.CASCADE)
    objects=models.Manager()
    def __str__(self):
        return self.classe_nom +""+str(self.departement_select.titre)
    
class Points(models.Model):
    classe=models.ForeignKey(Classes,on_delete=models.CASCADE)
    fichier=models.FileField(upload_to='photo/',blank=True,null=True)

    status=models.BooleanField(default=False) 
    
class Students(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField(upload_to='etudiant/image',null=True,blank=True)
    address=models.TextField(null=True,blank=True)
    etudiant_prenom=models.CharField(max_length=1000,null=True,blank=True)
    etudiant_groupe_sanguin=models.CharField(max_length=1000,null=True,blank=True)
    etudiant_date_de_naissance=models.CharField(max_length=1000,null=True,blank=True)
    etudiant_lieu_de_naissance=models.CharField(max_length=1000,null=True,blank=True)
    etudiant_nationalite=models.CharField(max_length=1000,null=True,blank=True)
    select_class = models.ForeignKey(Classes, on_delete=models.DO_NOTHING,default='',null=True,blank=True)
    student_roll = models.CharField(max_length=1000,null=True,blank=True)
    status=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminHOD.objects.create(admin=instance)
        if instance.user_type==2:
            Students.objects.create(admin=instance,etudiant_prenom='',etudiant_date_de_naissance='',etudiant_lieu_de_naissance='',etudiant_nationalite='',etudiant_groupe_sanguin='',select_class=Classes.objects.get(id=1),address="",profile_pic="",gender="",student_roll="")
@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminhod.save()
    if instance.user_type==2:
        instance.students.save()