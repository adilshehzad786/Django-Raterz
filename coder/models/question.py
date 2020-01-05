# -*- coding: utf-8 -*-


from django.db import models
from django.conf import settings

from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from coder.models.Tag import Tag
from coder.models.time import TimeStampedModel
class Question(models.Model):

    title = models.CharField(
        _('Title'), max_length=200)

    slug = models.SlugField(
        _('Slug'), max_length=200, unique=True)



    STATUS_CHOICES = (
        ('approved', _('Approved')),
        ('duplicated', _('Duplicated')),
        ('pending', _('Pending')),
        ('on_hold', _('On Hold')),
        ('closed', _('Closed')),
        ('deleted', _('Deleted'))
    )
    status = models.CharField(
        _('Status'), max_length=20,
        choices=STATUS_CHOICES, default='approved')

    description = models.TextField(_('Description'))



    edited = models.BooleanField(
        _('Edited?'), default=False)





    def __str__(self):
        return self.title

    class Meta:

        verbose_name_plural = _('questions')



class QuestionSuggestedEdits(TimeStampedModel):
    question = models.ForeignKey(
        Question, related_name='suggested_edits_question',on_delete=models.CASCADE)

    editor = models.ForeignKey(
        User, related_name='suggested_edits_editor',on_delete=models.CASCADE)

    title = models.CharField(
        _('Title'), max_length=200)

    tags = models.ManyToManyField(
        Tag, related_name='suggested_edits_tags')

    STATUS_CHOICES = (
        ('approved', _('Approved')),
        ('rejected', _('Rejected')),
        ('pending', _('Pending'))
    )
    status = models.CharField(
        _('Status'), max_length=20,
        choices=STATUS_CHOICES, default='pending')

    description = models.TextField(_('Description'))

    comment = models.TextField(_('Revision Comment'))

    @property
    def slug(self):
        return slugify(self.title)

    class Meta:
        verbose_name_plural = _('question suggested edits')
        ordering = ['-created']
