from django.urls import path, include
from supporter import views

app_name = 'supporter'
urlpatterns = [
    path('create', views.edit_or_create, name='create'),
    path('index', views.index, name='index'),
    path('<int:supporter_pk>/', include([
        path('details', views.details, name='details'),
        path('edit', views.edit_or_create, name='edit'),
        path('change-cw', views.change_cw, name='change_cw'),
        path('create-contact', views.upsert_contact, name='create_contact'),
        path('contact/<int:contact_pk>', include([
            path('update', views.upsert_contact, name='update_contact')
        ]))
    ]))
]
