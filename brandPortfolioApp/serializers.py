from rest_framework import serializers
from .models import ContactMessage, EmailFromFooter

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

class EmailFromFooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailFromFooter
        fields = '__all__'
