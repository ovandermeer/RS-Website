from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
     path('', views.get_name, name="form"),
     path('results/', views.results, name="results")
]
