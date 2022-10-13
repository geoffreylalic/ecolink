from django.urls import path

from publications.views import PublicationsView, PublicationDetailView, SuppliesView, DemandsView

urlpatterns = [
    path('', PublicationsView.as_view(), name='list_create_publication'),
    path('<int:pk>/', PublicationDetailView.as_view(), name='retrieve_update_destroy_publication'),
    path('supplies/', SuppliesView.as_view(), name='supplies_publication'),
    path('demands/', DemandsView.as_view(), name='demands_publication'),
]

