
from django.urls import path, include
from . import views





urlpatterns = [




    path('download_file/', views.download_file, name='download_file'),

]