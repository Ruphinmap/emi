# Generated by Django 4.0 on 2022-03-22 11:24

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[(1, 'HOD'), (2, 'Student')], default=1, max_length=100)),
                ('status', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Appropos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appropos', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='article/photo')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('classe_nom', models.CharField(max_length=1000)),
                ('classe_code', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='evenements/photo/')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Emi',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('emi_phone', models.CharField(blank=True, max_length=254, null=True)),
                ('emi_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('emi_adresse', models.CharField(max_length=254)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Evenements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='evenements/photo')),
                ('video', models.FileField(blank=True, null=True, upload_to='evenements/photo')),
                ('status', models.BooleanField(default=False)),
                ('jour', models.CharField(blank=True, max_length=10000, null=True)),
                ('mois', models.CharField(blank=True, max_length=10000, null=True)),
                ('heure', models.CharField(blank=True, max_length=10000, null=True)),
                ('lieu', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Horaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fichier', models.FileField(blank=True, null=True, upload_to='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAr',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.FileField(blank=True, null=True, upload_to='arriereplan/photo')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_etudiants', models.CharField(blank=True, max_length=10485760, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Opportunites',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='evenements/photo/')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Partenaires',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('photo', models.FileField(blank=True, null=True, upload_to='evenements/photo')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prof_prenom', models.CharField(max_length=1000)),
                ('prof_nom', models.CharField(max_length=1000)),
                ('prof_postnom', models.CharField(max_length=1000)),
                ('texte', models.TextField()),
                ('grade_ac', models.CharField(max_length=1000)),
                ('image', models.FileField(blank=True, null=True, upload_to='evenements/photo/')),
                ('position', models.CharField(blank=True, max_length=10000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Profs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomb_prof', models.CharField(blank=True, max_length=10485760, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titre', models.CharField(max_length=100)),
                ('contenu', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='evenements/photo')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gender', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(blank=True, null=True, upload_to='etudiant/image')),
                ('address', models.TextField(blank=True, null=True)),
                ('etudiant_prenom', models.CharField(blank=True, max_length=1000, null=True)),
                ('etudiant_groupe_sanguin', models.CharField(blank=True, max_length=1000, null=True)),
                ('etudiant_date_de_naissance', models.CharField(blank=True, max_length=1000, null=True)),
                ('etudiant_lieu_de_naissance', models.CharField(blank=True, max_length=1000, null=True)),
                ('etudiant_nationalite', models.CharField(blank=True, max_length=1000, null=True)),
                ('student_roll', models.CharField(blank=True, max_length=1000, null=True)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emi.customuser')),
                ('select_class', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='emi.classes')),
            ],
        ),
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fichier', models.FileField(blank=True, null=True, upload_to='photo/')),
                ('status', models.BooleanField(default=False)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emi.classes')),
            ],
        ),
        migrations.AddField(
            model_name='classes',
            name='departement_select',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emi.departement'),
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='emi.customuser')),
            ],
        ),
    ]
