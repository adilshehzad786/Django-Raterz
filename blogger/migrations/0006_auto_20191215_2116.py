# Generated by Django 2.2.6 on 2019-12-15 16:16

from django.db import migrations
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0005_auto_20191215_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
    ]