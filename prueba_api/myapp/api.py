from .models import EmailTemplate, SMTPConfiguration
from rest_framework import viewsets, permissions
from .serializers import EmailTemplateSerializer, SMTPConfigurationSerializer

class EmailTemplateViewSet(viewsets.ModelViewSet):
    queryset = EmailTemplate.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmailTemplateSerializer

class SMTPConfigurationViewSet(viewsets.ModelViewSet):
    queryset = SMTPConfiguration.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = SMTPConfigurationSerializer
  
