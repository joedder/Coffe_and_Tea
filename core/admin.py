from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,CategoryProduct,Product,Comment

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(CategoryProduct)
admin.site.register(Product)
admin.site.register(Comment)