

from django.db import models

from accounts.models import Profile

class Publication(models.Model):
    TYPE_CHOICES = (
        ('supply', 'supply'),
         ('demand', 'demand'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES,  max_length=6, blank=True, null=True)
    photos = models.ImageField(null=True, blank=True, upload_to='media')
    limit_date = models.DateField(null=True)
    price = models.DecimalField(null=True, blank=True, max_digits=999, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)
    is_pro = models.BooleanField(default=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, blank=True, null=True, related_name='created')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey('accounts.Profile', on_delete=models.CASCADE, blank=True, null=True, related_name='updated')