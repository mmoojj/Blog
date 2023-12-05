
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin  
from blog.models import Article , Category
from django.urls import reverse_lazy , reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import User
from django.contrib.auth import views
from .forms import UserModelForm
from .mixins import FieldMixin , FormMixin , UpdateMixin , CategoryMixin , check_is_superuser
# Create your views here.

# @login_required
# def home(request):
#     return render(request, 'registration/home.html')

@check_is_superuser
def change_category_state(request, pk):
    cat = get_object_or_404(Category, pk=pk)
    if cat.status:
        cat.status = False
    else:
        cat.status = True
    cat.save()    
    return HttpResponseRedirect(reverse('account:category'))
            
    

# show list of articles
class Home(LoginRequiredMixin , ListView):
    template_name ="registration/home.html"
    
    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)
        
class ArticleCreateView(LoginRequiredMixin , FieldMixin ,FormMixin, CreateView):
    model = Article
    # fields  use this in dispatch       
    template_name ="registration/article-create-update.html" 
    
  
    
class ArticleUpdateView(UpdateMixin , FieldMixin , UpdateView):
    model = Article
    # fields  use this in dispatch       
    template_name ="registration/article-create-update.html"  
    
    
class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy("account:home")  
    template_name = "registration/article_confirm_delete.html" 
    
              

# show list of categories        
class CategoryList(LoginRequiredMixin , CategoryMixin , ListView):
    template_name ="registration/categoey-list.html"
    model = Category
          
class CategoryUpdateView(CategoryMixin , UpdateView):
    model = Category
    fields = ["parent","title","slug","status","position"]
    # fields  use this in dispatch       
    template_name ="registration/category-create-update.html"        
 
class CategoryCreateView(CategoryMixin , CreateView):
    model = Category
    fields = ["parent","title","slug","status","position"]
    # fields  use this in dispatch       
    template_name ="registration/category-create-update.html"
    
class CategoryDeleteView(CategoryMixin,DeleteView):
    model = Category
    success_url = reverse_lazy("account:category")  
    template_name = "registration/category_confirm_delete.html"         
            
        

 
class Profile(LoginRequiredMixin,UpdateView):
    model = User
    # fields  use this in dispatch 
    # fields = ['username','email','first_name','last_name','spetial_user','is_author']
    form_class=UserModelForm    
    template_name ="registration/profile.html"
    success_url=reverse_lazy("account:profile")
    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)
    
    def get_form_kwargs(self):
        kwargs = super(Profile,self).get_form_kwargs()
        kwargs.update({
           'user':self.request.user 
        })
        return kwargs   
    
class Login(views.LoginView):
    def get_success_url(self):
        if self.request.user.is_superuser or self.request.user.is_author:
            return reverse_lazy("account:home") 
        else:
            return reverse_lazy("account:profile")     
    

class password_change(views.PasswordChangeView):
    success_url = reverse_lazy("account:password_change_done")
               

        
                
