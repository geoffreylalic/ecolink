from django.db import models

# from accounts.models import Profile


class Publication(models.Model):

    TYPE_CHOICES = (
        ('supply', 'supply'),
        ('demand', 'demand'),
    )

    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=255,null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(choices=TYPE_CHOICES,  max_length=6, blank=True)
    photos = models.ImageField()
    limit_date = models.DateField(null=True)
    price = models.DecimalField(null=True, blank=True, max_digits=999, decimal_places=2)
    quantity = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    # updated_by = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True)