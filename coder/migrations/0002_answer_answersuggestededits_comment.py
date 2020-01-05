# Generated by Django 2.2.6 on 2020-01-01 11:50

import coder.models.content_type
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='Object id')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('edited', models.BooleanField(default=False, verbose_name='Edited?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_author', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name_plural': 'comments',
                'ordering': ['-created'],
            },
            bases=(models.Model, coder.models.content_type.ContentTypeToGetModel),
        ),
        migrations.CreateModel(
            name='AnswerSuggestedEdits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('rejected', 'Rejected'), ('pending', 'Pending')], default='pending', max_length=20, verbose_name='Status')),
                ('description', models.TextField(verbose_name='Description')),
                ('comment', models.TextField(verbose_name='Revision Comment')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_edits_answer', to='coder.Question')),
                ('editor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggested_edits_answer_editor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'answer suggested edits',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('approved', 'Approved'), ('duplicated', 'Duplicated'), ('pending', 'Pending'), ('on_hold', 'On Hold'), ('closed', 'Closed'), ('deleted', 'Deleted')], default='approved', max_length=20, verbose_name='Status')),
                ('description', models.TextField(verbose_name='Description')),
                ('edited', models.BooleanField(default=False, verbose_name='Edited?')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_author', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answer_editor', to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_question', to='coder.Question')),
            ],
            options={
                'verbose_name_plural': 'answers',
                'ordering': ['-created'],
            },
        ),
    ]
