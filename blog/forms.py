from django import forms
from .models import BlogComment


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
