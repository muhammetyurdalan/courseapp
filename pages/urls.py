from django.urls import path
from pages import views


urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('about',views.about),
    path('contact',views.contact)
]
