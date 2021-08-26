from django.contrib import admin
from .models import BlogPost, BlogComment


class BlogPostAdmin(admin.ModelAdmin):
    """
    Setup Blog Post section of Admin Panel
    """

    list_display = (
                    'title',
                    'created_on',
                    'image',
    )

    search_fields = (
                     'title',
                     'body_text',
    )


class BlogCommentAdmin(admin.ModelAdmin):
    """
    Setup Blog Comment section of Admin Panel
    """
    list_display = (
        'user',
        'blog_post',
        'comment',
        'created_on',
    )

    search_fields = (
        'user',
        'comment',
    )


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
