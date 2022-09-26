from django.contrib import admin

from accounts.models import Profile, Company


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    model = Profile

class CompanyAdmin(admin.ModelAdmin):
    list_display = ( 'name',)
    model = Company

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Company, CompanyAdmin)
