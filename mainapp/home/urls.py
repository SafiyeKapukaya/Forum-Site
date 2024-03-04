from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('threads',views.threads,name='threads'),
    path('threadlist/',views.thread_list,name='threadlist'),
    path('addthread/',views.createpost , name = "createpost"),
    path('login',views.login_view,name='login'),
    path('register',views.register_view,name='register'),
    path('logout',views.logout_view,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('mainpage/',views.home, name = 'load'),
    path('create_reply/<int:post_id>/', views.create_reply, name='create_reply'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),

]