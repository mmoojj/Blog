from django.contrib import admin

from .models import Article , Category , IpAddress
from jalali_date.admin import ModelAdminJalaliMixin




# Register your models here.

admin.site.site_header ="پنل مدیریت"

def make_publish_or_draft(modeladmin,request,queryset,status,message):
    update = queryset.update(status=status)
    if update == 1:
        message = "{} شد".format(message)
    else:
        message = "{} شدند.".format(message)
    modeladmin.message_user(request,"{} مقاله {}".format(update, message)) 
        


def make_published(modeladmin, request, queryset):
    make_publish_or_draft(modeladmin,request,queryset,'p',"منتشر")        

def make_draft(modeladmin, request, queryset):
    make_publish_or_draft(modeladmin,request,queryset,'d',"پیش نویس")     


make_published.short_description = "انتشار مقالات انتخاب شده"
make_draft.short_description = "پیش نویس مقالات انتخاب شده"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['position','title','parent' ,'slug','status']
    list_filter = ['status']
    search_fields = ['title', 'slug']
    prepopulated_fields = {'slug':('title',)}
   

admin.site.register(Category, CategoryAdmin)

class ArticleAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ['title','thumbnail_admin','get_publish_jalali','is_spetial','status','author', 'category_to_str']
    list_filter = ['publish','status' , 'author']
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug':('title',)}
    ordering = ['-status', '-publish']
    actions = [make_published,make_draft]
    
    
    
    def category_to_str(self,obj):
        return [i for i in obj.category.filter(status=True)]
    
    category_to_str.short_description = "دسته بندی ها"
    
  
    
    
 
admin.site.register(Article, ArticleAdmin)
admin.site.register(IpAddress)
