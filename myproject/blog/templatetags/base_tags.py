from django import template
from ..models import Category  , Article
from django.db.models import Count , Q
from datetime import datetime , timedelta
register = template.Library()

@register.simple_tag
def title():
    return "وب لاگ جنگو";

@register.inclusion_tag("partial/category.html")
def category_nav_bar():
    return {
        "category": Category.objects.filter(status=True)
    }
    
@register.inclusion_tag("partial/sidebar.html")
def popular_article():
    last_month = datetime.today() - timedelta(days=30)
    return {
        "article": Article.objects.published().annotate(count = Count('hits',filter=Q(articlehits__created__gt=last_month))).order_by('-count','-publish'),
        "title":"مقالات پر بازدید ماه"
    }   
@register.inclusion_tag("partial/sidebar.html")
def popular_rating_article():
    return {
        "article": Article.objects.filter(ratings__isnull=False).order_by('-ratings__average'),
        "title": "مقالات با بیشترین امتیاز"
    }        