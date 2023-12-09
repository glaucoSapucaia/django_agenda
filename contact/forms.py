from typing import Any
from django import forms
from contact import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        label='Nome',
        min_length=5,
        required=True,
        help_text='Requerido',
    )
    last_name = forms.CharField(
        label='Sobrenome',
        min_length=5,
        required=True,
        help_text='Requerido',
    )
    email = forms.EmailField(
        label='email',
        min_length=5,
        required=True,
        help_text='Requerido',
    )
    username = forms.CharField(
        label='Usuário',
        min_length=5,
        required=True,
        help_text='Requerido',
    )
    password1 = forms.CharField(
        label='Senha',
        strip=False,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
            },
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        strip=False,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
            },
        ),
        help_text='Use a mesma a senha do primeiro campo.',
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username',
        )

    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)

        if commit:
            user.save()
        
        return user

    def clean(self) -> dict[str, Any]:
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError(
                        'As senhas devem ser iguais.',
                        code='invalid',
                    )
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError(
                        'Este email já existe',
                        code='invalid',
                    )
                )
            return email
        return email

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                    ValidationError(
                        errors,
                        code='invalid',
                    )
                )
        return password1

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=5,
        label='Nome',
        help_text='Requerido',
    )
    last_name = forms.CharField(
        required=True,
        min_length=5,
        label='Sobrenome',
        help_text='Requeido',
    )
    email = forms.EmailField(
        required=True,
        label='E-mail',
        help_text='requerido',
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
        required=False,
    )

    class Meta:
        model = models.Contact
        fields = ('first_name', 'last_name', 'phone',
                  'email', 'description', 'category', 'picture',)