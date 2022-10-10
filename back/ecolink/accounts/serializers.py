from rest_framework import serializers

from accounts.models import Profile, Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'email',
            'phone_number',
        )


class ProfileSerializer(serializers.ModelSerializer):
    company = serializers.SerializerMethodField()

    def get_company(self, instance):
        return 'teste_company'

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'favorites_publications',
            'owned_publications',
            'company',
        )
