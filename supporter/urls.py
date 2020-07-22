from django.urls import path, include
from supporter import views

app_name = 'supporter'
urlpatterns = [
    path('create', views.create, name='create'),
    path('list', views.index, name='index')
]
