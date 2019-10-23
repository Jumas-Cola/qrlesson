from django.urls import path
from . import views
from django.conf.urls import url
from django.views.generic import RedirectView
from .models import TeachingMethod, LessonPart


urlpatterns = [
    # path('', RedirectView.as_view(url=LessonPart.objects.all().first().url, permanent=True)),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('chosen_methods/', views.chosen_methods, name='chosen_methods'),
    path('qr_generator/', views.qr_generator, name='qr_generator'),
    path('qr_table/', views.qr_table, name='qr_table'),
    path('download/', views.download, name='download'),
    url(r'^upd_session/(?P<pk>[-\w]+)$', views.upd_session, name='upd_session'),
    url(r'^rmv_from_session/$', views.rmv_from_session, name='rmv_from_session'),
    url(r'^method/(?P<pk>[-\w]+)$', views.MethodDetailView.as_view(), name='method_detail'),
    url(r'^(?P<section>[\w]*)$', views.MethodListView.as_view(), name='method_list'),
]
