# Generated by Django 3.2.8 on 2021-10-09 05:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('p_name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Suplier')),
                ('p_telephone', models.CharField(max_length=10, verbose_name='Telephone')),
                ('p_email', models.CharField(max_length=100, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('code', models.CharField(max_length=8, primary_key=True, serialize=False, verbose_name='Code')),
                ('p_name', models.CharField(max_length=40, verbose_name='Product_name')),
                ('quantity', models.IntegerField()),
                ('movement', models.CharField(max_length=10, verbose_name='entry/exit')),
                ('price', models.CharField(max_length=15, verbose_name='Price')),
                ('category', models.CharField(choices=[('Des', 'Despensa'), ('Beb', 'Bebidas'), ('Mas', 'Para_Mascotas'), ('Beb', 'Para_Bebés'), ('AP', 'Aseo_Personal'), ('Lim', 'Limpieza')], default='Des', max_length=10)),
                ('description', models.CharField(max_length=200, verbose_name='Description')),
                ('prov_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authGestifyApp.proveedor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]