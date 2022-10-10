from rest_framework import serializers

from publications.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ('name', 'description', 'category', 'location', 'type', 'photos', 'limit_date', 'price', 'quantity')
