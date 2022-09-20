from django.urls import path
from . import views
urlpatterns=[
    path('',views.main_page,name='main'),
    path('check-t',views.Check_table , name='Check_t'),
    path("check-u/<str:pk>",views.check_u, name='check_u'),
    path('check-d/<str:pk>', views.check_d,name='check_d'),
]