from django.contrib import admin
from .models import User

class CustomUserAdmin(admin.ModelAdmin):
    fieldsets = (
        (None,{
            'fields': (
                'email',
                'password',
            )
        }),
        (None,{
            'fields': (
                'is_active',
                'is_admin',
            )
        }),
    )

admin.site.register(User, CustomUserAdmin)