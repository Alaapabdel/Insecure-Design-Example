from django.urls import path
from . import views

app_name = "lab4"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('details', views.details, name='details'),
    path('search', views.search, name='search'),
]
