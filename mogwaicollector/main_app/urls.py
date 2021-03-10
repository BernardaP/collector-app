from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mogwais/', views.mogwais_index, name='index'),
    path('mogwais/<int:mogwai_id>/', views.mogwais_detail, name='detail'),
    path('mogwais/<int:mogwai_id>/add_feeding/', views.add_feeding, name='add_feeding'),
]