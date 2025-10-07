from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'created_datetime')
    list_filter = ('created_datetime', 'username')
    search_fields = ('title', 'content', 'username')
    ordering = ('-created_datetime',)
