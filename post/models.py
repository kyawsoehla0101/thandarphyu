from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User




class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
            default='',
            editable=False,
        )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('category', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(
            default='',
            editable=False,
        )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('tagpost', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(
            default='',
            editable=False,
        )
    author = models.ForeignKey(User, on_delete=models.CASCADE ,default='Thandar Phru')
    content = models.TextField(null=True)
    short_content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to = 'static/%Y/%m/%d/postimages', blank= True,null=True,default='static/postimages/contactme.JPEG')
    tags = models.ManyToManyField(Tag)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    feature = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True, default='Thandar Phru')
    image= models.ImageField(upload_to="static/%Y/%m/%d/images")
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name
    