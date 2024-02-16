# Generated by Django 5.0.2 on 2024-02-14 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_postulante', models.CharField(max_length=144)),
                ('apellido_postulante', models.CharField(max_length=144)),
                ('edad_postulante', models.IntegerField(max_length=3)),
                ('direccion_postulante', models.TextField(blank=True, default='', null=True)),
                ('email_postulante', models.EmailField(blank=True, max_length=254, null=True)),
                ('telefono_postulante', models.CharField(max_length=10)),
                ('calificacion_postulante', models.CharField(max_length=3)),
            ],
        ),
    ]
