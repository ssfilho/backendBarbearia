from servicos.models import Service
from django.contrib import admin

# Register your models here.
class VisualizarServicos(admin.ModelAdmin):
    list_display = ('nome', 'tempo', 'valor')
    list_per_page = 20

admin.site.register(Service)

