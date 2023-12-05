from django.urls import path 
from .views import home , detail , category ,AuthorListView , ArticlePreview , SearchListView
from django.views.generic import TemplateView
app_name = 'blog'
urlpatterns = [
 path('',home,name="home")   ,
 path('page/<int:page>',home,name="home")   ,
 path('post/<slug:slug>',detail,name="post"),
 path('preview/<int:pk>',ArticlePreview.as_view(),name="preview"),
 path('about/',TemplateView.as_view(template_name="about.html"),name="about") ,
 path('contact/',TemplateView.as_view(template_name="contact.html"),name="contact"),
 path('category/<slug:slug>' , category,name="category") ,
 path('category/<slug:slug>/page/<int:page>' , category,name="category") ,
 path('author/<slug:username>' , AuthorListView.as_view(),name="author") ,
 path('author/<slug:username>/page/<int:page>' , AuthorListView.as_view(),name="author"),
 path('search/' , SearchListView.as_view(),name="search") ,
 path('search/<int:page>' , SearchListView.as_view(),name="search")  
 
]

