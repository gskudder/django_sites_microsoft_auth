# Generated by Django 2.2.5 on 2019-09-20 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microsoft_auth', '0004_siteconfiguration'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='authenticate_hook',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='callback_hook',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
