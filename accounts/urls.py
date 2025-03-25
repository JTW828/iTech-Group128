from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('home/', views.home, name='home'),
    path('stores/', views.store_list, name='store_list'),
    path('store/<int:store_id>/', views.store_detail, name="store_detail"),
    path('profile/', views.profile_view, name='profile'),
    path('store/<int:store_id>/like/', views.like_store, name='like_store'),
    path('store/<int:store_id>/favourite/', views.favourite_store, name='favourite_store'),
    
]