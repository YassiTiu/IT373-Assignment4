from django.contrib import admin
from .models import Author, Category, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'get_categories']
    list_filter = ['author', 'categories', 'published']
    search_fields = ['title', 'author__name']
    filter_horizontal = ['categories']
    readonly_fields = ['created_at']
    fieldsets = (
        ('Book Information', {
            'fields': ('title', 'author', 'published', 'isbn', 'pages')
        }),
        ('Categories & Description', {
            'fields': ('categories', 'description')
        }),
        ('Metadata', {
            'fields': ('created_at',)
        }),
    )
    
    def get_categories(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])
    get_categories.short_description = 'Categories'

