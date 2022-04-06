from django.db import models

from escrito.models import Autor


class Categoria_pub_multimedia(models.Model):
    
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


class Post_multimedia(models.Model):
    
    id = models.AutoField(primary_key = True)
    name = models.CharField(
        'Nombre del Set', max_length=255, null=False, blank=False                                        
    )
    pub_cre = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)
    autor = models.ForeignKey(
        Autor, 
        on_delete=models.CASCADE,
        related_name='Set',
    )
    categoria = models.ForeignKey(
        Categoria_pub_multimedia,
        on_delete=models.CASCADE,
    )
    archivo_multimedia = models.FileField(upload_to='video',max_length=255, blank=False, null=False)
    status = models.BooleanField('Publicado/No Publicado', default=True)
    description = models.CharField('Descripción', max_length=510, blank=False, null=True)
    slug = models.CharField('Slug', max_length=100, blank=False, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.name
