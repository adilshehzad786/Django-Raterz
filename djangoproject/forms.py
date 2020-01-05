from django import forms
from .models import File_Document,Teacher_Program,University_Program
from captcha.fields import CaptchaField
class DocumentForm(forms.ModelForm):
    class Meta:
        model = File_Document
        fields = ('description', 'file_document',)



class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name")
    contact_email = forms.EmailField(required=True, label="Email")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )

class Add_Teacher_Form(forms.ModelForm):

    class Meta:
        model = Teacher_Program
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})

class Add_University_Form(forms.ModelForm):

    class Meta:
        model =University_Program
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})


class CaptchaTestForm(forms.Form):

    captcha = CaptchaField()
