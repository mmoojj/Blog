
from django.urls import path
from .views import (
     Home , 
     ArticleCreateView ,
      ArticleUpdateView , 
     ArticleDeleteView ,
      CategoryCreateView , 
      CategoryList , 
      change_category_state ,
      CategoryUpdateView ,
       CategoryDeleteView , 
       Profile,

)


app_name = "account"
urlpatterns =[
    path('',Home.as_view(),name='home'),
    path('change/state/<int:pk>',change_category_state , name='state'),
    path('category/',CategoryList.as_view(),name='category'),
    path('article/create/',ArticleCreateView.as_view(),name='article_create'),
    path('category/create/',CategoryCreateView.as_view(),name='category_create'),
    path('category/update/<int:pk>',CategoryUpdateView.as_view(),name='category_update'),
    path('article/update/<int:pk>',ArticleUpdateView.as_view(),name='article_update'),
    path('profile/',Profile.as_view(),name='profile'),
    path('article/delete/<int:pk>',ArticleDeleteView.as_view(),name='article_delete'),
    path('category/delete/<int:pk>',CategoryDeleteView.as_view(),name='category_delete'),     
]
