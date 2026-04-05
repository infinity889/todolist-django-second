from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('update/<int:pk>/', views.update_view, name='update'),
    path('delete/<int:pk>/', views.delete_view, name='delete'),
    path('profile', views.profile_view, name='profile'),
    path('team', views.Team_view, name='team'),
    
]
