"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from Insta.views import HelloWorld, PostListView, PostDetailView, PostCreatView, PostUpdateView,PostDeleteView,addLike,UserDetailView,addComment,toggleFollow,EditProfile

urlpatterns = [
    path('index', HelloWorld.as_view(), name='HelloWorld'),
    path('', PostListView.as_view(), name='index'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreatView.as_view(), name='make_post'),
    path('post/edit/<int:pk>/',PostUpdateView.as_view(),name='post_update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
    path('like', addLike , name='addlike'),
    path('user/<int:pk>/',UserDetailView.as_view(),name='user_detail'),
    path('comment/<int:pk>/',addComment,name='addcomment'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('edit_user/<int:pk>/', EditProfile.as_view(), name='edit_profile'),
]
