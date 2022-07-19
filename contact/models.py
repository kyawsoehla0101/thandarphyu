from django.db import models

# Create your models here.
class Contact(models.Model):
  address = models.CharField(max_length=250)
  email = models.CharField(max_length=150)
  phone = models.CharField(max_length=20)
#   latitude = models.DecimalField(max_digits=9, decimal_places=6)
#   longitude = models.DecimalField(max_digits=9, decimal_places=6)
  
  class Meta:
    ordering = ('-id',)
    verbose_name = 'Contact'
    verbose_name_plural = 'Contact'
    
  def __str__(self):
    return self.email