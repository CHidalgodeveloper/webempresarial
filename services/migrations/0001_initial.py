# Generated by Django 4.2.4 on 2023-08-31 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titulo')),
                ('subtitle', models.CharField(max_length=100, verbose_name='Subtitulo')),
                ('image', models.ImageField(upload_to='services', verbose_name='imagen')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='modificacion')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servivcios',
                'ordering': ['-created'],
            },
        ),
    ]
