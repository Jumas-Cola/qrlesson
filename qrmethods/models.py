from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid


class TeachingMethod(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text='Уникальное ID для данного метода'
    )

    title = models.CharField(
        max_length=1000,
        help_text='Название педагогического приёма',
        verbose_name='Заголовок'
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    description = models.TextField(
        help_text='Описание педагогического приёма',
        verbose_name='Описание'
    )

    lesson_part = models.ForeignKey(
        'LessonPart',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Фрагмент урока'
    )

    def __str__(self):
        return self.title

    def get_preview(self):
        len_preview = 200
        if len(self.description) > len_preview:
            preview_string = self.description[:len_preview] + '...'
        else:
            preview_string = self.description
        return preview_string

    def get_reading_time(self):
        return len(self.description.replace(' ', '')) // 120

    def get_absolute_url(self):
        return reverse('method_detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Метод обучения'
        verbose_name_plural = 'Методы обучения'


class LessonPart(models.Model):
    name = models.CharField(
        max_length=1000,
        help_text='Название раздела'
    )

    description = models.TextField(
        help_text='Описание раздела'
    )

    url = models.CharField(
        max_length=500,
        help_text='Ссылка на раздел'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('method_list', args=[str(self.url)])

    class Meta:
        verbose_name = 'Фрагмент урока'
        verbose_name_plural = 'Фрагменты урока'
