from distutils.command import upload
from ckeditor.fields import RichTextField

from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


"""Here is the db models for the DIIG blog."""

class Autor(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre Autor', max_length=255, null=False, blank=False)
    status = models.BooleanField('Activo/Desactivado', default=True)
    pub_cre = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.name
        

class Categoria_pub_escrita(models.Model):
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(
        'Nombre de la categoria', max_length=100, null=False, blank=False
    )
    status = models.BooleanField('Categoria Activada/Desactivada', default=True)
    pub_cre = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.name


class Post_escrito(models.Model):
    
    id = models.AutoField(primary_key=True)
    title = CharField('Titulo', max_length=90, blank=False, null=False)
    slug = models.CharField('Slug', max_length=100, blank=False, null=False)
    description = models.CharField('Descripción', max_length=510, blank=False, null=False)
    content = RichTextField()
    image = models.ImageField(upload_to='img', blank=True, null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria_pub_escrita, on_delete=models.CASCADE)
    status = models.BooleanField('Publicado/No Publicado', default=True)
    pub_cre = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    pub_mod = models.DateField('Fecha Modificación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title