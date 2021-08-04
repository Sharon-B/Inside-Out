from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderLineItem


# Post save signal function
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update or create.
    Receives post_save signals from OrderLineItem
    """
    instance.order.update_total()


# Post delete signal function
@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update order total on lineitem delete.
    Receives post_delete signals from OrderLineItem
    """
    instance.order.update_total()
