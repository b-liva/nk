from django.urls import path, include
from case import views

app_name = 'case'
urlpatterns = [
    path('create/', views.create_case, name='create_case'),
    path('index/', views.index_case, name='index_case'),
    path('illness/', include([
        path('create/', views.create_illness, name='create_illness'),
        path('index/', views.index_illnesses, name='index_illness'),
    ])),
]
