
from django.urls import path, include
from . import views

urlpatterns = [
path('login/', views.signup_login, name='log'),
path('change_pass/', views.change_password, name='changepass'),
path('logout/', views.logout, name='logout'),
path('forget-password/', views.forget_password, name="forget"),

]