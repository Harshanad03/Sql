from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('s',views.shop),
     path('html/', views.html),
     path('text',views.text),
     path('para/<str:name>',views.para),
]