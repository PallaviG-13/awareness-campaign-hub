from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('campaign/<int:id>/', views.campaign_detail, name='campaign_detail'),
    path('create/', views.create_campaign, name='create_campaign'),
    path('join/<int:id>/', views.join_campaign, name='join_campaign'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', views.register, name='register'),

]
