from django.contrib import admin

# Register your models here.

from news.models import Articles

admin.site.register(Articles)