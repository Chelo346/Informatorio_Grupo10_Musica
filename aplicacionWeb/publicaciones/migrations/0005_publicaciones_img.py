# Generated by Django 4.2.7 on 2023-12-24 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0004_publicaciones_subtitulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicaciones',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes_publicaciones/'),
        ),
    ]
