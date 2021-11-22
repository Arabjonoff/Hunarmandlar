from django.contrib import admin
from .models import *
# Register your models here.
from parler.admin import TranslatableAdmin


@admin.register(Category)
class CategoryAdmin(TranslatableAdmin):
    list_display = ['title', 'slug']
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}

admin.site.register(Product)