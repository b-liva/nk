from django.urls import path, include
from caseworker.models import CaseWorker
from caseworker import views

app_name = 'caseworker'
urlpatterns = [
    path('create/', views.edit_or_create, name='create'),
    path('index/', views.index, name='index'),
    path('<int:cw_pk>/', include([
        path('details/', views.details, name='details'),
        path('edit/', views.edit_or_create, name='edit'),
    ])),
]