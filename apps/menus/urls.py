from django.urls import path
from . import views

urlpatterns = [
    path('', views.renderHome, name='home'),
    path('menu/<str:pk>/', views.menu, name="menu"),
    path('delete-option/<str:pk>/<str:bi>', views.deleteOption, name='delete-option'),
    path('update-option/<str:pk>/<str:bi>', views.updateOption, name='update-option'),
]