from django import forms
from contact import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=5,
        label='Nome',
    )
    last_name = forms.CharField(
        required=True,
        min_length=5,
        label='Sobrenome',
    )
    email = forms.EmailField(
        required=True,
        label='E-mail',
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2',
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError(
                    'Este email já existe',
                    code='invalid',
                )
            )
        return email

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