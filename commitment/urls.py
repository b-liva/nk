from django.urls import path
from commitment import views

app_name = 'commitment'
urlpatterns = [
    path('create', views.create, name='create'),
    path('index', views.index, name='index')
]