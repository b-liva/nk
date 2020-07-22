from recipient import views
from django.urls import path, include

app_name = 'recipient'

urlpatterns = [
    path('recipient/', include([
        path('create/', views.create_recipient, name='create_recipient'),
        path('index/', views.index_recipients, name='index_recipient'),
    ])),
    path('illness/', include([
        path('create/', views.create_illness, name='create_illness'),
        path('index/', views.index_illness, name='index_illness'),
    ])),
]
