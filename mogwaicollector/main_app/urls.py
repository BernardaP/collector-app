from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mogwais/', views.mogwais_index, name='index'),
    path('mogwais/new/', views.mogwais_new, name='new'),
    path('mogwais/<int:mogwai_id>/', views.mogwais_detail, name='detail'),
    path('mogwais/<int:mogwai_id>/edit/', views.mogwais_edit, name='edit'),
    path('mogwais/<int:mogwai_id>/delete/', views.mogwais_delete, name='delete'),
    path('mogwais/<int:mogwai_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('mogwais/<int:mogwai_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('mogwais/<int:mogwai_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
    path('accounts/signup/', views.signup, name='signup'),
]