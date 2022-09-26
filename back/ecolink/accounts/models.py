from django.contrib.auth import get_user_model
from django.db import models

from publications.models import Publication

User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    favorites_publications = models.ForeignKey(Publication, on_delete=models.CASCADE, blank=True, null=True, related_name='user_favorites_publications')
    owned_publications = models.ForeignKey(Publication, on_delete=models.CASCADE, blank=True, null=True, related_name='user_owned_publications')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
