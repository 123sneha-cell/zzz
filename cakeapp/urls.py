from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('logn',views.logn,name='logn'),
    path('add',views.admin_add_cake,name='add')
]