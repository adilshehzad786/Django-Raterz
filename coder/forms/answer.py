from django import forms

from martor.widgets import AdminMartorWidget
from coder.models.answer import Answer


class AnswerForm(forms.ModelForm):

    class Meta:
        model = Answer
        fields = ['description', ]
        widgets = {'description': AdminMartorWidget()}