# Generated by Django 5.0 on 2023-12-27 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0006_alter_publicaciones_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='imagen',
            field=models.ImageField(upload_to='posts'),
        ),
    ]
