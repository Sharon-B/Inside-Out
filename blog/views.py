from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import BlogPost, BlogComment
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
        if comment_form.is_valid() and request.user.is_authenticated:
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
    if request.user.is_superuser:

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.user = request.user
                blog_post.save()
                messages.success(request, 'Blog added successfully!')
                return redirect(reverse('blog_detail', args=[blog_post.id]))
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog failed to add.')
        else:
            form = BlogForm()
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'blog/add_blog.html'

    context = {
        'form': form,
    }

    return render(request, template, context)


# Edit Blog Post
@login_required
def edit_blog(request, blog_post_id):
    """
    Allow an admin user to edit a product to the store
    """
    if request.user.is_superuser:

        blog_post = get_object_or_404(BlogPost, pk=blog_post_id)

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blog_post)
            if form.is_valid():
                form.save()
                messages.success(request, 'Blog post updated successfully!')
                return redirect(reverse('blog_detail', args=[blog_post.id]))
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog post failed to update.')
        else:
            form = BlogForm(instance=blog_post)
            messages.info(request, f'Editing {blog_post.title}')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    template = 'blog/edit_blog.html'

    context = {
        'form': form,
        'blog_post': blog_post,
    }

    return render(request, template, context)


# Delete Blog Post
@login_required
def delete_blog_post(request, blog_post_id):
    """
    Allow an admin user to delete a blog post
    """
    if request.user.is_superuser:
        blog_post = get_object_or_404(BlogPost, pk=blog_post_id)
        blog_post.delete()
        messages.success(request, 'Blog post deleted!')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    return redirect(reverse('blog'))


# Delete Comment
@login_required
def delete_comment(request, comment_id):
    """
    Allow an admin user to delete a comment
    """
    if request.user.is_superuser:
        comment = BlogComment.objects.get(pk=comment_id)
        comment.delete()
        messages.success(request, 'Comment deleted!')
    else:
        messages.error(request, 'Sorry, you do not have permission for that.')
        return redirect(reverse('home'))

    return redirect('blog')
