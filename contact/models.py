from django.db import models


class Contact(models.Model):

    class Meta:
        verbose_name_plural = 'Contact Messages'

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return self.subject
