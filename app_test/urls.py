from django.urls import path, re_path
from django.contrib import admin
from django.conf.urls.static import static
from .views import *
# from Websiite.test_project import settings


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('show/<slug:slug_dir>/', ShowDirection.as_view(), name='show'),
    path('about/', about, name="about"),
    path('schedule/', schedule, name="schedule"),
    path('presentation/', presentation, name="presentation"),
    path('news/', news, name="news"),
    path('form/', form_feedback, name='form'),
    path('test/', DataForms.as_view(), name='test'),
    path('test_out/', form_test, name='testout'),
    path('rabbit/', rabbits, name='rabbit'),
    path('post/', post, name="post"),
    path('vk/', vk, name="vk"),
    path('wa/', wa, name="wa"),
    path('tg/', tg, name="tg"),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#
# handler_404 = pageNotFound