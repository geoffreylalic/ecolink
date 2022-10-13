from rest_framework import serializers

from accounts.serializers import ProfileSerializer
from publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    photos = serializers.SerializerMethodField()

    def get_email(self, instance):
        profile = instance.created_by
        return ProfileSerializer(profile).data.get('email')

    def get_phone_number(self, instance):
        profile = instance.created_by
        return ProfileSerializer(profile).data.get('phone_number')

    def get_photos(self, instance):
        request = self.context.get('request')
        if instance.photos is None:
            return None
        else:
            a = instance
            photos_url = instance.photos.url
            b =request.build_absolute_uri(photos_url)
            return request.build_absolute_uri(photos_url)
            # return request.build_absolute_url(photos_url)


    class Meta:
        model = Publication
        fields = (
        'id', 'name', 'description', 'category', 'location', 'type', 'photos', 'limit_date', 'price', 'quantity',
        'created_at', 'email', 'phone_number')
