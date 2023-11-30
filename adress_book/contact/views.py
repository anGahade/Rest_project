from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from contact.models import Contact, ContactGroup, Events
from contact.serializers import ContactSerializer, ContactGroupSerializer, EventSerializer
from rest_framework import filters


class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
    # permission_classes = [IsAuthenticated]


class ContactGroupViewSet(ModelViewSet):
    queryset = ContactGroup.objects.prefetch_related('contacts').all()
    serializer_class = ContactGroupSerializer


class EventViewSet(ModelViewSet):
    queryset = Events.objects.prefetch_related('contacts').all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['location', 'title']





