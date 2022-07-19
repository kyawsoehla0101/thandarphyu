from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255, null=True, blank= True)
    content = QuillField()
    image = models.ImageField(upload_to='aboutimages', null=True, blank=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'About'
        verbose_name_plural = 'About'
    
    def __str__(self):
        return self.title