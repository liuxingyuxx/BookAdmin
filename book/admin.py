from django.contrib import admin
from .models import Book, Author

# Register your models here.
#适用于外键
class BookInline(admin.TabularInline):
    model = Book 
    extra = 4

class AuthorInline(admin.TabularInline):
    model = Author 
    extra = 4 
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_url','book_lever' )
    search_fields = ('book_name',) 
    ordering = ('-book_name','-book_lever')
    #inlines = [AuthorInline]
    #这个是添加书籍，改变书籍显示的
    #fields = ('book_name','book_url')
    list_filter = ('book_author',)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_name','valuation' )
    search_fields = ('author_name',)
    field = ("author_name",)
    inlines = [BookInline]
    
#admin.site.register(Book, BookAdmin)

admin.site.register(Author, AuthorAdmin)
