from unicodedata import category
from django.contrib import admin
from .models import Category,Tag,Gallery,Post
# Register your models here.
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Gallery)
admin.site.register(Post)