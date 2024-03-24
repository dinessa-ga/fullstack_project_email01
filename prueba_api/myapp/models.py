from django.db import models

# Create your models here.

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    header_image = models.ImageField(upload_to='email_headers/')
    footer_image = models.ImageField(upload_to='email_footers/')

    def __str__(self):
        return self.subject
    
class SMTPConfiguration(models.Model):
    smtp_server = models.CharField(max_length=200)
    port = models.IntegerField()
    smtp_user = models.CharField(max_length=200)
    smtp_password = models.CharField(max_length=200)
    recipient_email = models.EmailField()

def __str__(self):
        return self.smtp_server