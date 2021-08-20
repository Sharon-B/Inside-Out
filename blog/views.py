from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from .forms import BlogCommentForm


# All blog posts view
def all_blog_posts(request):
    """
    A view to show the blog page
    """

    blog_posts = BlogPost.objects.all()

    template = 'blog/blog.html'

    context = {
        'blog_posts': blog_posts,
    }

    return render(request, template, context)


# Blog detail view
def blog_detail(request, blog_post_id):
    """
    A view to show individual blog post and comments.
    """
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    comments = blog_post.comments.all()

    comment_form = BlogCommentForm()

    template = 'blog/blog_detail.html'

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_form': comment_form,
    }

    return render(request, template, context)
