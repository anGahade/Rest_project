from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from contact.models import Contact, ContactGroup, Events


class ContactSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)
    street = serializers.CharField(max_length=30)
    url = serializers.URLField(max_length=200)
    phone = serializers.CharField(max_length=30, validators=[UniqueValidator(queryset=Contact.objects.all())])
    image = serializers.ImageField(required=False)

    class Meta:
        model = Contact
        fields = '__all__'


class ContactGroupSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    class Meta:
        model = ContactGroup
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    contacts = serializers.SerializerMethodField()

    class Meta:
        model = Events
        fields = '__all__'
        # exclude = ['contacts']

    def get_contacts(self, obj):
        contacts = obj.contacts.all()

        serialized_contacts = [
            {
                'id': contact.id,
                'first_name': contact.first_name,
                'last_name': contact.last_name,
            }
            for contact in contacts
        ]
        return serialized_contacts


