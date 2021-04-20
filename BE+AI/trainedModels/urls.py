from django.urls import path

from . import views

urlpatterns = [
    path('upload', views.uploadModel, name='uploadModel'),
    path('listAll', views.listAll, name='listAll')
    #path('success', views.success, name='success')
]
