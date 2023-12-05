
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
from django.views.generic import ListView , DetailView
# from django.contrib.auth.models import User
from account.models import User
from .models import Article , Category
from account.mixins import UpdateMixin
from django.db.models import Count , Q
from datetime import datetime , timedelta
# Create your views here.

def home(request,page=1):
    last_month = datetime.today() - timedelta(days=30)
    articles = Article.objects.published().annotate(count = Count('hits',filter=Q(articlehits__created__gt=last_month))).order_by('-count','-publish')
    

    paginator = Paginator(articles, 3)
    
    
    content = paginator.get_page(page)
    return render(request, 'index.html' , {'articles': content})



def detail(request , slug):
    article = get_object_or_404(Article, slug=slug , status='p')
    ip_address = request.user.ip_address
    if ip_address not in article.hits.all():
        article.hits.add(ip_address)
    return render(request, 'post.html', {'article': article})


def category(request, slug , page=1):
    category = get_object_or_404(Category, slug=slug , status=True)
    article_list = category.articles.published()
    paginator = Paginator(article_list, 3) 
    articles = paginator.get_page(page)
    return render(request, 'category.html', {'category': category , 'articles':articles})

# class Home(ListView):
#     queryset = Article.objects.published().annotate(count=Count('hits')).order_by('-count','-publish')
#     paginate_by=3
    


class ArticlePreview(UpdateMixin,DetailView):
    template_name="article_detail.html"
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article, pk=pk)
        
    

class AuthorListView(ListView):
    paginate_by=3
    template_name = "author_list.html"
    
    def get_queryset(self):
        global author
        username = self.kwargs.get('username')
        author = get_object_or_404(User , username=username)
        return author.articles.published()
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['author'] = author
        return context
    
class SearchListView(ListView):
    paginate_by=2
    template_name = "search_list.html"
    
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context    
    
    