# Generated by Django 2.2.6 on 2019-12-19 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freecourses', '0004_auto_20191216_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_link',
            field=models.URLField(blank=True, db_index=True, max_length=300, unique=True),
        ),
    ]
