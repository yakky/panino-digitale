from django.contrib import admin

from .models import Panino


@admin.register(Panino)
class PaninoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'prezzo')
    search_fields = ('nome',)
