from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


from coder.models.question import Question
from coder.models.time import TimeStampedModel
from coder.models.comment import Comment

@python_2_unicode_compatible
class AnswerQuerySet(models.QuerySet):

    def approved(self):
        """ whenever the answer is correct according to the author of the question """
        return self.filter(status='approved')

    def duplicated(self):
        """ mark/flag the answer as duplicated answer """
        return self.filter(status='duplicated')

    def pending(self):
        return self.filter(status='pending')

    def on_hold(self):
        return self.filter(status='on_hold')

    def closed(self):
        return self.filter(status='closed')

    def deleted(self):
        return self.filter(status='deleted')

@python_2_unicode_compatible
class Answer(TimeStampedModel):
    author = models.ForeignKey(
        User, related_name='answer_author',on_delete=models.CASCADE)

    question = models.ForeignKey(
        Question, related_name='answer_question',on_delete=models.CASCADE)

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

    editor = models.ForeignKey(
        User, blank=True, null=True,
        on_delete=models.SET_NULL, related_name='answer_editor')

    objects = AnswerQuerySet.as_manager()

    def __str__(self):
        _title = _('%(author)s comment on %(question)s')
        return _title % {'author': self.author, 'question': self.question}

    def edits_object(self):
        answer = self
        qs = AnswerSuggestedEdits.objects.filter(answer=answer)
        if qs.exists():
            return qs.first()
        return answer


    @property
    def has_offset_comments(self):
        """ to check the answer has a offset comments or not """
        return self.get_comments_offset().exists()

    class Meta:
        verbose_name_plural = _('answers')
        ordering = ['-created']

class AnswerSuggestedEdits(TimeStampedModel):
    editor = models.ForeignKey(
        User, related_name='suggested_edits_answer_editor',on_delete=models.CASCADE)

    answer = models.ForeignKey(
        Question, related_name='suggested_edits_answer',on_delete=models.CASCADE)

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

    class Meta:
        verbose_name_plural = _('answer suggested edits')
        ordering = ['-created']