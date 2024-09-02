from django.urls import path

from . import views

urlpatterns = [
    path('', views.DogList.as_view()),
    path('', views.DogDetail.as_view()),
]
