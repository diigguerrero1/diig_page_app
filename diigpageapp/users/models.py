from django.contrib.auth.models import User
from django.db import models

class Profile_User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone_number = models.CharField(max_length=20, blank=True)
    created = models.DateField(auto_now=False, auto_now_add=True)
    modified = models.DateField(auto_now=True, auto_now_add=False)

    instagram = models.URLField(max_length=200, blank=True)
    twitter = models.URLField(max_length=200, blank=True)
    linkedin = models.URLField(max_length=200, blank=True)
    facebook = models.URLField(max_length=200, blank=True)
    tiktok = models.URLField(max_length=200, blank=True)
    youtube = models.URLField(max_length=200, blank=True)
    spotify = models.URLField(max_length=200, blank=True)
    mixcloud = models.URLField(max_length=200, blank=True)
    soundcloud = models.URLField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user


class Autor(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Profile_User, on_delete=models.CASCADE)
    status = models.BooleanField('Autor Activo/Inactivo', default=True)
    pub_cre = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return self.user


class comentario(models.Model):

    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Profile_User, on_delete=models.CASCADE)
    contenido = models.CharField('Contenido', max_length=300, blank=False, null=False)
    status = models.BooleanField('Autor Activo/Inactivo', default=True)
    pub_cre = models.DateField('Fecha de Creación', auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.user, self.contenido