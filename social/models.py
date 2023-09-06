from django.db import models

# Create your models here.

class Social(models.Model):
    key=models.SlugField(verbose_name='nombre clave',max_length=50, unique=True)
    name=models.CharField(max_length=50, verbose_name='red social')
    url=models.URLField(verbose_name='enlace',null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name="modificacion")

    class Meta:
        verbose_name="Red Social"
        verbose_name_plural="Redes Sociales"
        ordering=["-created"]

    def __str__(self):
        return self.name
