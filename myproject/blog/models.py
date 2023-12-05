from django.db import models
from django.utils import timezone
from jalali_date import datetime2jalali
from extensions.utils import number_converter
from django.utils.html import format_html
from account.models import User
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from star_ratings.models import Rating

# my managers

class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')
    
class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)    


class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="ای پی کاربر")

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name ='دسته بندی'
        verbose_name_plural ="دسته بندی ها"
        ordering =['parent__id','position']
        
    parent = models.ForeignKey('self',default=None , null=True,blank=True,on_delete=models.SET_NULL,related_name="children",verbose_name="زیر دسته")
    title = models.CharField(max_length=200,verbose_name="عنوان")
    slug = models.SlugField(max_length=100 , unique=True , verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="نمایش داده شود؟")
    position = models.IntegerField(verbose_name="پوزیشن")
    
    
    def get_absolute_url(self):
        return reverse("account:category")    
    
    def __str__(self):
        return self.title    
    
    objects = CategoryManager()

class Article(models.Model):
    class Meta:
        verbose_name ='مقاله'
        verbose_name_plural ="مقالات"
        ordering =['-publish']
    
    STATUS_CHOICES = (
        ('d','پیش نویس'),
        ('p','منتشر شده'),
    )
    
    author= models.ForeignKey(User, null=True , on_delete=models.SET_NULL , related_name="articles" , verbose_name="نویسنده")
    title = models.CharField(max_length=200,verbose_name="عنوان")
    slug = models.SlugField(max_length=100 , unique=True , verbose_name="آدرس")
    category = models.ManyToManyField(Category, blank=True , verbose_name="دسته بندی" , related_name="articles")
    description = models.TextField(verbose_name="محتوا")
    sumbnail = models.ImageField(upload_to='images',verbose_name="تصویر")
    publish = models.DateTimeField(default=timezone.now,verbose_name="تاریخ انتشار")
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)
    is_spetial = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    status = models.CharField(max_length=1 , choices=STATUS_CHOICES , verbose_name="وضعیت")
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IpAddress,through="ArticleHits", related_name="hits", blank=True,verbose_name="بازدید ها")
    ratings = GenericRelation(Rating, related_query_name='foos')
    
    def __str__(self):
        return self.title
    
    def get_publish_jalali(self):
        return number_converter(datetime2jalali(self.publish).strftime('%a : %d / %b / %Y ساعت %H:%M'))
    
    def thumbnail_admin(self):
        return format_html("<img width=100 height=75 style='border-radius: 5px;' src='{}' /> ".format(self.sumbnail.url))
	
    def get_absolute_url(self):
        return reverse("account:home")
 
    def category_to_str(self):
        return ",".join([i.title for i in self.category.filter(status=True)])
 
    get_publish_jalali.short_description = "تاریخ انتشار"
    thumbnail_admin.short_description = "تصویر"
    objects = ArticleManager()
    
class ArticleHits(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IpAddress,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True )
       
    
