from django.contrib import admin
from postdisplay.models import postview

class postdisplayadmin(admin.ModelAdmin):
    list_display = ('post_title','post_user')

admin.site.register(postview,postdisplayadmin)


# Register your models here.
