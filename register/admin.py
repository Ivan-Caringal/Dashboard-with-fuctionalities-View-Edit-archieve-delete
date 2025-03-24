from django.contrib import admin
from .models import CustomUser
#here you edit hte djjango default admin site

from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'mobile', 'barangay', 'position', 'barangayCode', 'role', 'approval_status')
    list_filter = ('role', 'approval_status')  # Filter users by role and approval status
    search_fields = ('username', 'email', 'name')  # Search by username, email, or name
    list_editable = ('approval_status', 'role')  # Edit approval_status & role in the list view

    # Display approval_status & role as dropdowns in the admin form
    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'name', 'email', 'mobile', 'barangay', 'position', 'barangayCode')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),
        ('Approval & Role', {
            'fields': ('approval_status', 'role')  # Add role to admin form
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib.admin import AdminSite
from django.contrib.auth.views import LoginView
from django.urls import path
from .forms import CustomAdminLoginForm

class CustomAdminSite(AdminSite):
    login_form = CustomAdminLoginForm

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('login/', LoginView.as_view(authentication_form=CustomAdminLoginForm), name='login'),
        ]
        return custom_urls + urls

# Replace Django's default admin site
admin_site = CustomAdminSite(name='custom_admin')

