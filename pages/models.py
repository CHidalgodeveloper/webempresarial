from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Page(models.Model):
    title=models.CharField(max_length=50,verbose_name="Titulo")
    content=RichTextField(verbose_name="contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name='creacion')
    updated=models.DateTimeField(auto_now=True, verbose_name="modificacion")

    class Meta:
        verbose_name="Pagina"
        verbose_name_plural="Paginas"
        ordering=["title"]

    def __str__(self):
        return self.title

