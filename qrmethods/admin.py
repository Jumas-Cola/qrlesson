from django.contrib import admin
from .models import TeachingMethod, LessonPart


@admin.register(TeachingMethod)
class TeachingMethodAdmin(admin.ModelAdmin):
    list_display = ('title', 'lesson_part', 'author', 'id')
    list_filter = ('lesson_part', 'author')


# admin.site.register(TeachingMethod)
admin.site.register(LessonPart)
