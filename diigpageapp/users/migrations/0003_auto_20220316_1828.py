# Generated by Django 3.2.12 on 2022-03-16 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escrito', '0004_auto_20220316_1828'),
        ('multimedia', '0005_alter_post_multimedia_autor'),
        ('users', '0002_auto_20220316_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile_user',
            name='user',
        ),
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='comentario',
        ),
        migrations.DeleteModel(
            name='Profile_User',
        ),
    ]
