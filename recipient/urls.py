from recipient import views
from django.urls import path, include

app_name = 'recipient'

urlpatterns = [
    path('recipient/', include([
        path('create/', views.create_recipient, name='create_recipient'),
        path('index/', views.index_recipients, name='index_recipient'),
    ])),
]
