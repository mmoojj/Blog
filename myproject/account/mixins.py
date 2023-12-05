from django.http import Http404
from django.shortcuts import get_object_or_404 , redirect
from blog.models import Article
from functools import wraps

class FieldMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = ["author","title","slug","category","description",'is_spetial',"sumbnail","publish","status"] 
        elif request.user.is_author:
            self.fields = ["title","slug","category","description",'is_spetial',"sumbnail","publish"]
            
        else:
            raise Http404("you can`t access this page")
        return super().dispatch(request, *args, **kwargs)
    
    
class FormMixin:
    
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = 'd'
        return super().form_valid(form)           
    
class UpdateMixin:
    def dispatch(self, request,pk, *args, **kwargs):
        article = get_object_or_404(Article,pk=pk)
        if article.author==request.user and article.status=='d' or request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)  
        else:
            raise Http404("you can`t access this page")
        
class CategoryMixin:
    def dispatch(self, request, *args, **kwargs):
        if  request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)  
        elif request.user.is_author:
            raise Http404("you can`t access this page")
        else:
            return redirect("account:profile")    
          
    
   
# function mixin when use function in views
def check_is_superuser(view_func):
    @wraps(view_func)
    def _wrapper_view(request,pk, *args, **kwargs):
        if request.user.is_superuser:
            return view_func(request,pk, *args, **kwargs)
        else:
            raise Http404("you can`t access this page") 

    return _wrapper_view
    
    