from django.contrib import admin
from .models import Author,Post,Reply

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","lastname","registerdate")

admin.site.register(Author,AuthorAdmin)
admin.site.register(Post)
admin.site.register(Reply)