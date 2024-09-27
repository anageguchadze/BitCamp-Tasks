from django.contrib import admin
from .models import Chef, Recipe

# Register your models here.
admin.site.register(Chef)
admin.site.register(Recipe)