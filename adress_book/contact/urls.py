from contact.views import ContactViewSet, ContactGroupViewSet, EventViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')
router.register('contact-group', ContactGroupViewSet, basename='contact_group')
router.register('events', EventViewSet, basename='event')


urlpatterns = router.urls


