from dataclasses import field
from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    services = {
        ('----', 'Select Services'),
        ('Website Development', 'Website Development'),
        ('Mobile App Development', 'Mobile App Development'),
        ('Software Development', 'Software Development'),
        ('UI/UX Designing', 'UI/UX Designing'),
        ('AI/ML', 'AI/ML'),
        ('IOT Development', 'IOT Development'),
        ('Cloud Deployment', 'Cloud Deployment'),
        ('Product Maintainence', 'Product Maintainence'),
        ('Other', 'Other'),
    }
    service = forms.ChoiceField(
        initial='----', choices=services, widget=forms.Select(attrs={'class': 'form-control'}))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeHolder': "Enter Business Email"}))
    number = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeHolder': "Enter Mobile Number"}))

    class Meta:
        model = Contact
        exclude = ['date']
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeHolder': "Enter First Name"}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeHolder': "Tell us more about your project, needs, and timeline."}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeHolder': "Business Name Or URL"})
        }
