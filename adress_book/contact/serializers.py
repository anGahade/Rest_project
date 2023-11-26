from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from contact.models import Contact


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

