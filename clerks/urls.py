from django.urls import path, include
from . import views




urlpatterns = [



    path('clerks/<str:slug>',views.clerk_package,name='clerk'),
    path('details/<int:slug>',views.package_details,name='detail_pack'),

    path('fatora/',views.fatora,name='fat'),

    path('notification/', views.notification_details, name='notify'),

    path('download_sub/', views.export_users_xls, name='download_excel'),

]