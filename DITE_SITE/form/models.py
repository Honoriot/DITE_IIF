from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.

class FORM(models.Model):
    Name = models.CharField(help_text='User Name', max_length=15)
    Email = models.EmailField(max_length=256)
    Phone_No = models.IntegerField(null=True)
    College_Name = models.TextField(null=True)
    #created_date = models.DateTimeField(default=timezone.now)
    #published_date = models.DateTimeField(blank=True, null=True)
    Suggestions = models.TextField(help_text="Improvement is important..")
    Featured = models.BooleanField(default=False, null=True)