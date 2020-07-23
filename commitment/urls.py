from django.urls import path, include
from commitment import views

app_name = 'commitment'
urlpatterns = [
    path('create/', views.edit_or_create, name='create'),
    path('index/', views.index, name='index'),
    path('<int:commitment_pk>/', include([
        path('details', views.details, name='details'),
        path('edit', views.edit_or_create, name='edit'),
    ]))
]