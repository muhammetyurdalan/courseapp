from django.urls import path
from . import views


urlpatterns = [
    path("login",views.user_login,name="user_login_url"),
    path("logout",views.user_logout,name="user_logout_url"),
    path("register",views.user_register,name="user_register_url"),
   
]
