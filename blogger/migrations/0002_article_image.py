# Generated by Django 2.2.6 on 2019-12-14 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]
