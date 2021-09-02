from django import forms
from .models import Category, Product
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """
    Creates a product form, used for adding a product
    """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        display_names = [(c.id, c.get_display_name()) for c in categories]

        self.fields['category'].choices = display_names
        for field in self.fields.values():
            field.widget.attrs['class'] = 'admin-form'
