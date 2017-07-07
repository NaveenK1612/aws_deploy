from django.contrib import admin
from aws_deploy.polls import models


admin.site.register(models.Question, admin.ModelAdmin)
admin.site.register(models.Choice, admin.ModelAdmin)
# Register your models here.
