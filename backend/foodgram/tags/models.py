from colorfield.fields import ColorField
from django.db import models


class Tags(models.Model):
    """Модель тегов."""
    name = models.CharField(
        'Название',
        max_length=200,
        unique=True,
    )
    color = ColorField(
        'Цвет',
        default='#FF0000',
        max_length=7,
        unique=True,
    )
    slug = models.SlugField(
        'Описание',
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ('name',)

    def __str__(self):
        return self.name[:10]
