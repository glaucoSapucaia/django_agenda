from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    first_name = models.CharField(max_length=50, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    phone = models.CharField(max_length=50, verbose_name='Telefone')
    email = models.EmailField(max_length=50, verbose_name='E-mail')
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Criado em")
    description = models.TextField(blank=True, verbose_name='Descrição',)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/Ym/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='Categoria',
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.pk} {self.first_name} {self.last_name}'
