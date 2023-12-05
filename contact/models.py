from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/Ym/')
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'{self.pk} {self.first_name} {self.last_name}'
