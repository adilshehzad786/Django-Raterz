# Generated by Django 2.2.6 on 2019-11-23 19:55

from django.db import migrations, models
import djangoproject.custom_azure


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191104_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', null=True, storage=djangoproject.custom_azure.AzureMediaStorage, upload_to='profile_pics'),
        ),
    ]
