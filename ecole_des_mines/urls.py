"""ecole_des_mines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from emi.views import *
from emi import views, HodViews,StudentViews
from ecole_des_mines import settings
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('edite_profile/<id>/', HodViews.edite_profile, name="edite_profile"),
    path('edite_profile_save', HodViews.edite_profile_save,name="edite_profile_save"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.acceuil,name="acceuil"),
    path('show_login',views.ShowLoginPage,name="show_login"),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('student_home',StudentViews.student_home,name="student_home"),
    path('appercu',HodViews.appercu,name="appercu"),
    path('delete_profile/<profile_id>/', HodViews.delete_profile, name="delete_profile"),
    path('add_emi_save',HodViews.add_emi_save,name="add_emi_save"),
    path('admin_profile', HodViews.admin_profile,name="admin_profile"),
    path('admin_profile_save', HodViews.admin_profile_save,name="admin_profile_save"),
    path('telecharge_horaire', StudentViews.telecharge_horaire,name="telecharge_horaire"),
    path('telecharge_valve', StudentViews.telecharge_valve,name="telecharge_valve"),
    path('creer_article', HodViews.creer_article,name="creer_article"),
    path('creer_article_save', HodViews.creer_article_save,name="creer_article_save"),
    
    path('creer_partenaire', HodViews.creer_partenaire,name="creer_partenaire"),
    path('creer_partenaire_save', HodViews.creer_partenaire_save,name="creer_partenaire_save"),
    path('creer_project', HodViews.creer_project,name="creer_project"),

    path('creer_project_save', HodViews.creer_project_save,name="creer_project_save"),
       
    path('creer_opportunite', HodViews.creer_opportunite,name="creer_opportunite"),

    path('creer_opportunite_save', HodViews.creer_opportunite_save,name="creer_opportunite_save"),
    
    
    path('creer_evenement', HodViews.creer_evenement,name="creer_evenement"),
    path('lire_article/<id>/',HodViews.lire_article,name='lire_article'),
    
    path('update_article/<id>/',HodViews.update_article,name='update_article'),
    path('update_article_save',HodViews.update_article_save,name='update_article_save'),
    path('update_departement/<id>/',HodViews.update_departement,name='update_departement'),

    path('update_departement_save',HodViews.update_departement_save,name='update_departement_save'),
    path('update_opportunite/<id>/',HodViews.update_opportunite,name='update_opportunite'),
    path('update_opportunite_save',HodViews.update_opportunite_save,name='update_opportunite_save'),
    
    path('update_project/<id>',HodViews.update_project,name='update_project'),

    path('update_project_save',HodViews.update_project_save,name='update_project_save'),

    path('update_evenement/<id>/',HodViews.update_evenement,name='update_evenement'),

    path('update_evenement_save',HodViews.update_evenement_save,name='update_evenement_save'),
    
    path('lire_profile/<id>/',HodViews.lire_profile,name='lire_profile'),
    path('lire_evenement/<id>/',HodViews.lire_evenement,name='lire_evenement'),
    path('lire_departement/<id>/',HodViews.lire_departement,name='lire_departement'),
    path('lire_project/<id>/',HodViews.lire_project,name='lire_project'),
    path('lire_opportunite/<id>/',HodViews.lire_opportunite,name='lire_opportunite'),
    path('creer_evenement_save', HodViews.creer_evenement_save,name="creer_evenement_save"),
    
    path('departement', HodViews.departement,name="departement"),

    path('departement_save', HodViews.departement_save,name="departement_save"),
    path('promotion', HodViews.promotion,name="promotion"),
    path('promotion_save', HodViews.promotion_save,name="promotion_save"),
    path('point', HodViews.point,name="point"),
    path('point_save', HodViews.point_save,name="point_save"),
    
    path('creer_image', HodViews.creer_image,name="creer_image"),

    path('creer_image_save', HodViews.creer_image_save,name="creer_image_save"),
        
    path('creer_horaire', HodViews.creer_horaire,name="creer_horaire"),

    path('creer_horaire_save', HodViews.creer_horaire_save,name="creer_horaire_save"),
    
    path('add_profile',HodViews.add_profile,name="add_profile"),

    path('add_profile_save',HodViews.add_profile_save,name="add_profile_save"),
    path('add_student',HodViews.add_student,name="add_student"),

    path('add_student_save',HodViews.add_student_save,name="add_student_save"),
    path('import_etudiant',HodViews.import_etudiant,name="import_etudiant"),


    path('import_etudiant_save',HodViews.import_etudiant_save,name="import_etudiant_save"),
    
    path('nombre_etudiant',HodViews.etudiant,name="nombre_etudiant"),

    path('nombre_etudiant_save',HodViews.etudiant_save,name="nombre_etudiant_save"),
    
    path('nombre_prof',HodViews.prof,name="nombre_prof"),

    path('nombre_prof_save',HodViews.prof_save,name="nombre_prof_save"),
    

    path('delete_partenaire/<id>/', HodViews.delete_partenaire, name="delete_partenaire"),
    path('delete_student/<id>/', HodViews.delete_student, name="delete_student"),
    
    path('delete_article/<id>/', HodViews.delete_article, name="delete_article"),
    path('delete_evenement/<id>/', HodViews.delete_evenement, name="delete_evenement"),
    
    path('delete_project/<id>/', HodViews.delete_project, name="delete_project"),
    
    path('delete_departement/<id>/', HodViews.delete_departement, name="delete_departement"),
    
    path('delete_opportunite/<id>/', HodViews.delete_opportunite, name="delete_opportunite"),
    
    path('apropos',HodViews.appropos,name="apropos"),

    path('appropos_save',HodViews.appropos_save,name="appropos_save"),
    path('contacte',HodViews.contacte,name="contacte"),
    path('add_emi',HodViews.add_emi,name="add_emi"),
    path('apropos_nous',HodViews.apropos_nous,name="apropos_nous"),
    
    path('student_profile', StudentViews.student_profile, name="student_profile"),

    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    path('all_articles',HodViews.all_articles,name='all_articles'),
    path('all_departements',HodViews.all_departements,name='all_departements'),
    path('all_profiles',HodViews.all_profiles,name='all_profiles'),
    path('all_opportunites',HodViews.all_opportunites,name='all_opportunites'),
    path('all_projects',HodViews.all_projects,name='all_projects'),
    path('all_evenements',HodViews.all_evenements,name='all_evenements'),
    path('liste_etudiant',HodViews.liste_etudiant,name='liste_etudiant'),
    
    




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


