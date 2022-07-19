from django.db import models

# Create your models here.
class Hero(models.Model):
  title = models.CharField(max_length=200)
  subtitle = models.CharField(max_length=300)
  description = models.TextField()
  image = models.ImageField(upload_to='images')
  
  class Meta:
    ordering = ('-id',)
    verbose_name = 'Hero'
    verbose_name_plural = 'Hero'
    
  def __str__(self):
    return '{0} {1}'.format(self.title, self.subtitle)