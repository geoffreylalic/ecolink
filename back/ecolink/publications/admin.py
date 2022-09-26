from django.contrib import admin

# Register your models here.
from publications.models import Publication


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    model = Publication

admin.site.register(Publication, PublicationAdmin)
