# dash/forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'category', 'email', 'phone_number', 'birthday', 'last_contact', 'work', 'note', 'instagram_handle', 'linkedin_url', 'uploaded_document', 'profile_picture']
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
            'last_contact': forms.DateInput(attrs={'type': 'date'}),
        }
