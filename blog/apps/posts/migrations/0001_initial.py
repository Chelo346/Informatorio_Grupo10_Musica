# Generated by Django 4.2.7 on 2023-11-24 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=355)),
                ('cuerpo', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
    ]
