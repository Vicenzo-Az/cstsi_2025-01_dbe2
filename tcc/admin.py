from django.contrib import admin
from tcc import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email',
    ordering = '-id',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 20
    list_max_show_all = 200
    list_editable = 'first_name', 'last_name', 'email',
    list_display_links = 'id',
