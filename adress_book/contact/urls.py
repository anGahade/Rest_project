from contact.views import ContactList, ContactDetailView
from django.urls import path

urlpatterns = [
    path('', ContactList.as_view(), name='contact_list'),
    path('/detail/<int:pk>/', ContactDetailView.as_view())
]
