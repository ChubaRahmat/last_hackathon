from django.contrib import admin
from .models import Post, Category, Comment

admin.site.register(Post)
admin.site.register(Comment)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name']
    prepopulated_fields = {'slug': ('name', )}