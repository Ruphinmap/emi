from django import forms
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Horaire
        exclude=('status',)
        fields = ('fichier',)
class PointForm(forms.ModelForm):
    class Meta:
        model = Points
        exclude=('status',)
        fields = ('classe','fichier',)  

class ArticlesForm(forms.Form):
    gender_choice=(
        ("True","Oui"),
        ("False","Non")
    )
    
    
    titre=forms.CharField(label="Titre",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    contenu=forms.CharField(label="Contenu",max_length=50000000000000000000000000000000000000000000000000000000000000000,widget=forms.Textarea(attrs={"class":"form-control"}))
    photo=forms.FileField(label="Photo",max_length=500,help_text="choisir uniquement si vous voulez remplacer l'ancienne ",widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    status=forms.ChoiceField(label="Publier ",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))

class DepartementForm(forms.Form):

    gender_choice=(

        ("True","Oui"),
        ("False","Non")
    )
    titre=forms.CharField(label="Titre",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    contenu=forms.CharField(label="Contenu",max_length=50000000000000000000000000000000000000000000000000000000000000000,widget=forms.Textarea(attrs={"class":"form-control"}))
    photo=forms.FileField(label="Photo",max_length=500,help_text="choisir uniquement si vous voulez remplacer l'ancienne ",widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    status=forms.ChoiceField(label="Publier ",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))



class OpportuniteForm(forms.Form):
    gender_choice=(

        ("True","Oui"),
        ("False","Non")
    )
    
    
    titre=forms.CharField(label="Titre",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    contenu=forms.CharField(label="Contenu",max_length=50000000000000000000000000000000000000000000000000000000000000000,widget=forms.Textarea(attrs={"class":"form-control"}))
    photo=forms.FileField(label="Photo",max_length=500,help_text="choisir uniquement si vous voulez remplacer l'ancienne ",widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    status=forms.ChoiceField(label="Publier ",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))




class ProjectForm(forms.Form):

    gender_choice=(
        ("True","Oui"),
        ("False","Non")
    )
    
    titre=forms.CharField(label="Titre",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    
    contenu=forms.CharField(label="Contenu",max_length=50000000000000000000000000000000000000000000000000000000000000000,widget=forms.Textarea(attrs={"class":"form-control"}))
    photo=forms.FileField(label="Photo",max_length=500,help_text="choisir uniquement si vous voulez remplacer l'ancienne ",widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    status=forms.ChoiceField(label="Publier ",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
 

class EvenementForm(forms.Form):

    gender_choice=(

        ("True","Oui"),
        ("False","Non")
    )
    
    
    titre=forms.CharField(label="Titre",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    jour=forms.CharField(label="Jour",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    mois=forms.CharField(label="Mois",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    lieu=forms.CharField(label="Lieu",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    heure=forms.CharField(label="Heure",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    contenu=forms.CharField(label="Contenu",max_length=5000000000000000000000000000000000,widget=forms.Textarea(attrs={"class":"form-control"}))
    
    photo=forms.FileField(label="Photo",max_length=500,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    video=forms.FileField(label="video",max_length=500,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    status=forms.ChoiceField(label="Publier ",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
class ProfilesForm(forms.Form):
    gender_choice=(
        ("True","Oui"),
        ("False","Non")
    )
    
    
    prof_prenom=forms.CharField(label="Prenom",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    prof_nom=forms.CharField(label="Nom",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    prof_postnom=forms.CharField(label="Postnom",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    grade_ac=forms.CharField(label="Grade Académique",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    position=forms.CharField(label="Position",max_length=1000,widget=forms.TextInput(attrs={"class":"form-control"}))
    texte=forms.CharField(label="Appropos du prof",max_length=50000000000000000000000000000000000000000000000000000000000000000,widget=forms.Textarea(attrs={"class":"form-control"}))
    image=forms.FileField(label="Photo",max_length=500,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
    status=forms.ChoiceField(label="Publier",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))