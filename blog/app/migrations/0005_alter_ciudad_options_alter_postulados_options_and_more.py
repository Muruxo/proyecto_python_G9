# Generated by Django 5.0.2 on 2024-02-20 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_ciudad_detallepostulante_empleo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='postulados',
            options={'verbose_name_plural': 'Postulados'},
        ),
        migrations.AlterModelOptions(
            name='publicacion',
            options={'verbose_name_plural': 'Publicaciones'},
        ),
    ]
