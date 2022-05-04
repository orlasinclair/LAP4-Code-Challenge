from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name = 'lazy-url-home'),
    path("<str:short>", views.RedirectedUrl, name="redirect")
]
