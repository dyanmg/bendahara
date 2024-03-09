from django.urls import path

from . import views

app_name = 'jurnal'

urlpatterns = [
    path('', views.index, name='index'),
    path('tambah', views.tambah, name='tambah'),
    path('simpan', views.simpan, name='simpan')
]