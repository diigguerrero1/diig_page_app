from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class Categoria_pub_multimediaResource(resources.ModelResource):
    class Meta:
        model = Categoria_pub_multimedia

class Categoria_pub_multimediaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'pub_cre')
    resource_class = Categoria_pub_multimediaResource

admin.site.register(Categoria_pub_multimedia, Categoria_pub_multimediaAdmin)


class Post_multimediaResource(resources.ModelResource):
    class Meta:
        model = Post_multimedia
    
class Post_multimediaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'pub_cre', 'categoria')
    resource_class = Post_multimediaResource

admin.site.register(Post_multimedia, Post_multimediaAdmin)
    