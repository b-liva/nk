from recipient import views
from django.urls import path, include

app_name = 'recipient'

urlpatterns = [
    path('recipient/', include([
        path('create/', views.edit_or_create, name='create_recipient'),
        path('index/', views.index_recipients, name='index_recipient'),
        path('<int:recipient_pk>/', include([
            path('details', views.details, name='details'),
            path('edit', views.edit_or_create, name='edit'),
        ]))
    ])),
]
