from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('top',views.index,name='index'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('UserEdit',views.UserEdit,name='UserEdit'),
    path('doSearch',views.doSearch,name='doSearch'),
    path('doUserEdit',views.doUserEdit,name='doUserEdit'),
    path('doUserUpdate',views.doUserUpdate,name='doUserUpdate'),
    path('doUserCreate',views.doUserCreate,name='doUserCreate'),
    path('Top',views.Top,name='Top'),
]