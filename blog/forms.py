from django import forms
from products.widgets import CustomClearableFileInput
from .models import BlogComment, BlogPost


class BlogCommentForm(forms.ModelForm):

    class Meta:
        model = BlogComment

        fields = (
            'comment',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs[
            'placeholder'] = 'Leave your comment here..'
        self.fields['comment'].label = 'Comment'
        self.fields['comment'].widget.attrs['class'] = 'comment-form'


class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = {
            'title',
            'body_text',
            'image',
        }

    field_order = ['title', 'body_text', 'image']

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'admin-form'
        self.fields['title'].widget.attrs['placeholder'] = 'Blog Title'
        self.fields['body_text'].widget.attrs['placeholder'] = 'Blog Content'
