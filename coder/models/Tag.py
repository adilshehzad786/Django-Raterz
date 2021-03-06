# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from coder.models.time import TimeStampedModel


@python_2_unicode_compatible
class Tag(TimeStampedModel):
    creator = models.ForeignKey(
        User, related_name='tag_creator',on_delete=models.CASCADE)

    title = models.CharField(
        _('Title'), max_length=200)

    slug = models.SlugField(
        _('Slug'), max_length=200, unique=True)

    short_description = models.TextField(
        _('Short Description'))

    wiki = models.TextField(
        _('Wiki'), null=True, blank=True)

    edited = models.BooleanField(
        _('Edited?'), default=False)

    editor = models.ForeignKey(
        User, blank=True, null=True,
        on_delete=models.SET_NULL, related_name='tag_editor')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = _('tags')
        ordering = ['-created']