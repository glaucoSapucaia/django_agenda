from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone',)
    search_fields = ('id', 'first_name', 'email',)
    ordering = ('-id',)
    list_display_links = ('id',)
    list_editable = ('first_name', 'email',)
    list_per_page = 10
    list_max_show_all = 100
