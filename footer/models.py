from django.db import models

# Create your models here.
class Social(models.Model):
    icon = models.ImageField(upload_to='icons',null=True,blank=True)
    name = models.CharField(max_length=100,null=True,blank=True)
    social_link = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name = 'Social'
        verbose_name_plural = 'Social'
    
    def __str__(self):
        return '{0} {1}'.format(self.name, self.social_link)

class Footer(models.Model):
    social = models.ManyToManyField(Social,blank=True)
    copyright = models.CharField(max_length=200,null=True,blank=True)
    website_name = models.CharField(max_length=200,null=True,blank=True)
    website_link = models.CharField(max_length=200,null=True,blank=True)

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'
    
    def __str__(self):
        return '{0} {1}'.format(self.id, self.copyright)