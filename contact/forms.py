from django import forms
from contact import models
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    ...

class ContactForm(forms.ModelForm):
    picture = forms.ImageField(
        label='Imagem',
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
            },
        ),
    )

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'picture',)