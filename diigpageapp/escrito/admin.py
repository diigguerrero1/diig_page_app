from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'status', 'pub_cre')
    resource_class = AutorResource

admin.site.register(Autor, AutorAdmin)


class Categoria_pub_escritaResource(resources.ModelResource):
    class Meta:
        model = Categoria_pub_escrita

class Categoria_pub_escritaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'status', 'pub_cre')
    resource_class = Categoria_pub_escritaResource

admin.site.register(Categoria_pub_escrita, Categoria_pub_escritaAdmin)


class Post_escritoResource(resources.ModelResource):
    class Meta:
        model = Post_escrito

class Post_escritoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title', 'slug']
    list_display = ('title', 'slug', 'pub_cre')
    resource_class = Post_escritoResource

admin.site.register(Post_escrito, Post_escritoAdmin)