import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from user_profiles.models import UserProfile


# Order Model
class Order(models.Model):
    """
    An Order model which creates an order number and includes the user details,
    date, delivery cost, order totals, the original cart and the stripe pid.
    """

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
                                     UserProfile,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=24, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    city_town = models.CharField(max_length=56, null=False, blank=False)
    county = models.CharField(max_length=56, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=16, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(
                                        max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0)
    order_total = models.DecimalField(
                                      max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(
                                      max_digits=10,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    original_cart = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
                                  max_length=254,
                                  null=False,
                                  blank=False,
                                  default='')

    def _generate_order_number(self):
        """
        Generate a random unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        including delivery costs where applicable
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0

        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the default save method to set the order number
        if it doesn't already exist
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Order Line Item Model
class OrderLineItem(models.Model):
    """
    A model for each item in the order whish includes which order
    it belongs to, the item, it's quantity and the total for that item.
    """

    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=8, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        """
        Override the default save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Product code {self.product.product_code} \
            on order {self.order.order_number}'
