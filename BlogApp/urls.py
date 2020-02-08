from django.urls import path
from . import views


urlpatterns = [
    path('',views.IndexView,name='home'),
    path('signup',views.SignUp,name='SignUp'),
    path('login',views.LogIn,name='LogIn'),
    path('like',views.like,name='like'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('newpost',views.newpost,name='newpost'),
    path('signout',views.SignOut,name='signout'),
    ]


