from django.contrib import admin
from .models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = (
                    'title',
                    'created_on',
                    'image',
    )

    search_fields = (
                     'title',
                     'body_text',
    )


admin.site.register(BlogPost, BlogPostAdmin)
