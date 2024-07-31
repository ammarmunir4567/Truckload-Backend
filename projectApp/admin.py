from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active', 'is_superuser')  # Add 'role' and any other fields you want to display
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  # Add custom fields in the admin detail view
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),  # Add custom fields in the admin create user form
    )

# Register the admin class with the associated model
admin.site.register(CustomUser, CustomUserAdmin)
