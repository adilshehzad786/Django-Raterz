# Generated by Django 2.2.6 on 2019-12-31 15:44

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0007_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name=(('Fun', 'Fun'), ('Knowledge', 'Knowledge'), ('Science', 'Science'))),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='Write Tags Relevant With Your Post E.g facebook,google,amazon . Tags Help in Boosting Posting SEO', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
