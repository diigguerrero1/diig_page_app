# Generated by Django 3.2.12 on 2022-04-06 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multimedia', '0007_auto_20220319_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='post_multimedia',
            name='description',
            field=models.CharField(max_length=510, null=True, verbose_name='Descripción'),
        ),
    ]
