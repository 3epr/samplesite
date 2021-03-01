from django.contrib import admin

from .models import Bb

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rublic')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Bb, BbAdmin)

from .models import Rublic

admin.site.register(Rublic)

# Register your models here.
