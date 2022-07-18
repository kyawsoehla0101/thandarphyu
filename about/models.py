from django.db import models
from django_quill.fields import QuillField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255, null=True, blank= True)
    content = QuillField()

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
    
    def __str__(self):
        return self.title