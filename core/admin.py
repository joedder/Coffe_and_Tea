from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,CategoryProduct,Product,Comment

# Register your models here.

admin.site.register(User, UserAdmin)

@admin.register(CategoryProduct)
class CategoryProductAdmin(admin.ModelAdmin):
    list_display=('name','description',)
    search_fields = ('name',)
    list_editable=("description",)
    list_filter = ('name',)
    list_per_page = 2
    #exclude=("description") #permite excluir campos de la vista del admin 

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','category', 'description','price','stock','image',)
    search_fields = ('name', 'category__name',)
    list_editable=('price','stock','description',"image",)
    list_filter = ('category', 'price',)
    list_per_page=2

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('user','product','body','created_at',)
    search_fields = ('user__username','product__name','body',)
    list_filter = ('created_at',)
    list_per_page=2
