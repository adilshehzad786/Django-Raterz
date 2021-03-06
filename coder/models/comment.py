# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


from coder.models.time import TimeStampedModel
from coder.models.content_type import ContentTypeToGetModel


@python_2_unicode_compatible
class Comment(TimeStampedModel, ContentTypeToGetModel):
    author = models.ForeignKey(
        User, related_name='comment_author',on_delete=models.CASCADE)

    content_type = models.ForeignKey(
        ContentType, related_name='comments',
        on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField(_('Object id'))

    content_object = GenericForeignKey('content_type', 'object_id')

    comment = models.TextField(_('Comment'))



    edited = models.BooleanField(
        _('Edited?'), default=False)

    def __str__(self):
        return '%s' % self.get_related_object()

    class Meta:
        verbose_name_plural = _('comments')
        ordering = ['-created']