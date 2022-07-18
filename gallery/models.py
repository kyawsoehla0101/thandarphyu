from django.db import models

# Create your models here.
class Gallery(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True, default='Thandar Phru')
    image= models.ImageField(upload_to="static/%Y/%m/%d/images")
    caption = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(auto_now=True,null=True,blank=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'
    
    def __str__(self):
        return '{0} {1}'.format(self.name, self.image)