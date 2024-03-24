# Generated by Django 5.0.3 on 2024-03-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('header_image', models.ImageField(upload_to='email_headers/')),
                ('footer_image', models.ImageField(upload_to='email_footers/')),
            ],
        ),
        migrations.CreateModel(
            name='SMTPConfiguration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('smtp_server', models.CharField(max_length=200)),
                ('port', models.IntegerField()),
                ('smtp_user', models.CharField(max_length=200)),
                ('smtp_password', models.CharField(max_length=200)),
                ('recipient_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
