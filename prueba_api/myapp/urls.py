from rest_framework import routers

from myapp.api import EmailTemplateViewSet, SMTPConfigurationViewSet

# Crear un enrutador
router = routers.DefaultRouter()

# Registrar las vistas en el enrutador
router.register('api/email-templates', EmailTemplateViewSet, 'emailTemplate' )
router.register('api/smtp-configurations', SMTPConfigurationViewSet, 'smtpConfiguration' )


urlpatterns = router.urls