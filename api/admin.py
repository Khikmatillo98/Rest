from django.contrib import admin
from .models import Book, Comment, User, Cart 

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category'] 



admin.site.register(Book, BookAdmin)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Cart)