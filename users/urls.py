from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_request, name="login"),
    path('register/', views.register, name="register"),
    #path('logout/', LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('edit/', views.edit, name="edit")
    ]