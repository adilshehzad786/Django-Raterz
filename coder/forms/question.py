# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.translation import ugettext_lazy as _

from martor.widgets import AdminMartorWidget


from coder.models.question import Question,QuestionSuggestedEdits


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title']
        widgets = {

            'title': forms.TextInput(attrs={'placeholder': _("What's your programming question? Be specific.")}),
            'description': AdminMartorWidget()
        }

# def __init__(self, *args, **kwargs):
#    super(QuestionForm, self).__init__(*args, **kwargs)
#    self.fields['tags'].widget.attrs = {'class': 'ui search fluid dropdown tags-dropdown'}


class QuestionSuggestedEditsForm(forms.ModelForm):

    class Meta:
        model = QuestionSuggestedEdits
        fields = ['title']
        widgets = {

            'title': forms.TextInput(attrs={'placeholder': _("What's your programming question? Be specific.")}),
            'description': AdminMartorWidget()
        }