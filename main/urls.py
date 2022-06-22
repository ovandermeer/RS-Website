from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('deities/', views.deities, name='deities'),
    path('rituals/', views.rituals, name='rituals'),
    path('about/', views.about, name='about'),
]
