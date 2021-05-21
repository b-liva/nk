from django.urls import path, include
from case import views

app_name = 'case'
urlpatterns = [
    path('create/', views.edit_or_create_case, name='create_case'),
    path('index/', views.index_case, name='index_case'),
    path('autocomplete', views.autocomplete, name='autocomplete'),
    path('<int:case_pk>/', include([
        path('details/', views.case_details, name='details'),
        path('edit/', views.edit_or_create_case, name='edit_case'),
    ])),
    path('illness/', include([
        path('create/', views.edit_or_create_illness, name='create_illness'),
        path('index/', views.index_illnesses, name='index_illness'),
        path('<int:illness_pk>/', include([
            path('details', views.illness_details, name='illness_details'),
            path('edit', views.edit_or_create_illness, name='illness_edit'),
        ]))
    ])),
]
