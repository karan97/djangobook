from django.contrib import admin

from . import models

class BooksAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(models.Books, BooksAdmin)  
