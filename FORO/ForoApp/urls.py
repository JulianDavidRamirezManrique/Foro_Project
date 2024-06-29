from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:user>/', views.profile, name='profile'),    
    path('profile/new/', views.profile_new, name='profile'),    
    path('profile/edit/<int:user>', views.profile_edit, name='profile_edit'),    
    path('profile/delete/<int:user>', views.profile_delete, name='profile_delete'),    
    path('threads/', views.threads, name='threads'),
    path('threads/create/', views.threads_create, name='threads_create'),
    path('threads/1',views.threads_show, name='threads_show'),
    path('threads/1/reply',views.threads_reply, name='threads_reply'),
]