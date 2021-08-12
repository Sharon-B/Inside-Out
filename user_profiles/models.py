from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# User profile
class UserProfile(models.Model):
    """
    User profile model for each user to maintain
    their default delivery info and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    default_full_name = models.CharField(max_length=50, null=True, blank=True)
    default_email = models.EmailField(max_length=254, null=True, blank=True)
    default_phone_number = models.CharField(max_length=24, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_city_town = models.CharField(max_length=56, null=True, blank=True)
    default_county = models.CharField(max_length=56, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)
    default_postcode = models.CharField(max_length=16, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create/update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Save profile for existing users:
    instance.userprofile.save()
