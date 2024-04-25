from datetime import date
from autoslug import AutoSlugField
from django.db import models

class postview(models.Model):
    post_title = models.CharField(max_length=50)
    post_user = models.CharField(max_length=20, default='')
    post_time = models.DateField(default=date.today)
    post_details = models.TextField(default='')
    slug = AutoSlugField(populate_from='post_title',unique=True,null=True,default=None)

# Create your models here.
