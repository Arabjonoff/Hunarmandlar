from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/profile/', views.profile, name='profile'),
    path("like/", views.like, name="like"),
]
