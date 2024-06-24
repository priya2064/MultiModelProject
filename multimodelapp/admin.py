from django.contrib import admin

from multimodelapp.models import Author, Book


# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','email']
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display=['title','name','published_date']
admin.site.register(Book,BookAdmin)

