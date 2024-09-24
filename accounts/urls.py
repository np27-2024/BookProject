from django.urls import path

from accounts import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("register/", views.register_user, name='register'),
    path("login/", views.login_user, name='login')


]
