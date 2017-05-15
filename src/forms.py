from django import forms
from upload.models import Document

class contactForm(forms.Form):
	name = forms.CharField(required=False, max_length=100, help_text='100 characters max.')
	email = forms.EmailField(required=True)
	comment = forms.CharField(required=True, widget=forms.Textarea)


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

