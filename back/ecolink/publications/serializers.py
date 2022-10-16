from rest_framework import serializers

from accounts.serializers import ProfileSerializer
from publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    photos = serializers.ImageField(required=False, allow_null=True, use_url=True)

    def get_email(self, instance):
        profile = instance.created_by
        # return ProfileSerializer(profile).data.get('email')
        return 'admin@ecolink.com'
    
    def get_phone_number(self, instance):
        profile = instance.created_by
        # return ProfileSerializer(profile).data.get('phone_number')
        return '07 98 18 19 77'
    class Meta:
        model = Publication
        fields = (
            'id', 'name', 'description', 'category', 'location', 'type', 'photos', 'limit_date', 'price', 'quantity',
            'created_at', 'email', 'phone_number')
