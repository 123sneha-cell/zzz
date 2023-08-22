from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('main_home',views.main_home,name='main_home'),
    path('logn',views.logn,name='logn'),
    path('add',views.admin_add_cake,name='add'),
    path('cake_view',views.cake_view,name='cake_view'),
    path('update/<id>',views.cake_update,name='cake_update'),
    path('cake_delete/<id>',views.cake_delete,name='cake_delete'),
    path('user_reg',views.user_reg,name='user_reg'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('user_view_cakes',views.user_view_cakes,name='user_view_cakes'),
    path('search',views.search,name='search'),
    path('more',views.more,name='more'),
     path('adminHome',views.adminHome,name='adminHome'),
      path('userHome',views.userHome,name='userHome'),
    path('admin_view_user',views.admin_view_user,name='admin_view_user')
]