from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/register/', views.RegisterView.as_view(), name='register'),
    path('dashboard/', views.DashboarView, name='dashboard')
]
