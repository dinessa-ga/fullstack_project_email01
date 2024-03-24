from rest_framework import serializers
from .models import EmailTemplate, SMTPConfiguration

class EmailTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailTemplate
        fields = ('id', 'subject', 'content', 'header_image','footer_image' )

class SMTPConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMTPConfiguration
        fields = ('id','smtp_server','port','smtp_user','smtp_password', 'recipient_email' )