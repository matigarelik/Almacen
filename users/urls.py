# Almacen\users\urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from users import views

urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('edit/', views.edit, name='edit')
]

