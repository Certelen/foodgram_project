# Generated by Django 3.2.19 on 2023-05-30 21:08

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_alter_tags_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=7, samples=None, unique=True, verbose_name='Цвет'),
        ),
    ]
