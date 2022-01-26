from django.contrib import admin
from blog.models import Post, Category
from projects.models import Project
# Register your models here.

# class PosAdmin(admin.ModelAdmin):
#     pass

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Project)