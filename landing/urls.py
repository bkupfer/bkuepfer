from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dog', views.dog_classifier, name='dog_classifier'),
]
