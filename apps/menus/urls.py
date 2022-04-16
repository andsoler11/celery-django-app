from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderHome, name='home'),
    path('menu/<str:pk>/', views.menu, name="menu"),
]