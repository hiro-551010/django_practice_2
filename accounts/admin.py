from django.contrib import admin
from .models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline, )
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