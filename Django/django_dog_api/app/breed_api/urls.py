from django.urls import path

from . import views

urlpatterns = [
    path('', views.BreedList.as_view()),
    path('<int:pk>', views.BreedDetail.as_view()),
]
