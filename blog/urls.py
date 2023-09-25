from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('blog_page/<str:blog_title>',views.blog_page,name='blog_page'),
]