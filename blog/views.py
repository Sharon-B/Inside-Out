from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost
from .forms import BlogCommentForm, BlogForm


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
    A view to show individual blog post, comments
    and to allow logged in users to leave a comment.
    """
    blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
    comments = blog_post.comments.all()
    new_comment = None

    if request.method == 'POST':
        comment_form = BlogCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = blog_post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'Comment added successfully!')
            return redirect(reverse('blog_detail', args=[blog_post.id]))
        else:
            messages.error(request, 'Please check the form for errors. \
                Comment failed to post.')
    else:
        comment_form = BlogCommentForm()

    template = 'blog/blog_detail.html'

    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }

    return render(request, template, context)


# Blog Admin:
# Add blog
@login_required
def add_blog_post(request):
    """
    Allow an admin user to add a blog post
    """

    form = BlogForm()

    template = 'blog/add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)
