from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from django_filters import rest_framework as filters
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response

from publications.models import Publication
from publications.serializers import PublicationSerializer


class PublicationsView(generics.ListCreateAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'type', 'category', )


class PublicationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.all()

    def destroy(self, request, *args, **kwargs):
        # soft delete
        pub = self.get_object()
        pub.is_active = False
        pub.save()
        return Response(data=self.get_serializer(pub).data, status=status.HTTP_204_NO_CONTENT)


class SuppliesView(generics.ListAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.filter(type='supply')

class DemandsView(generics.ListAPIView):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.filter(type='demand')
