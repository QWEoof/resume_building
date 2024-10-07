
from django import forms
from .models import Resume, Section

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'template']

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'content']
