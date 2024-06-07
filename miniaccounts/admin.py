from django.contrib import admin
from miniaccounts.models import ProfileInfo

@admin.register(ProfileInfo)
class ProfileInfoAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'bio',
        'acc_type',
        'country',
        'gender',
        'dob',
        'email',
        'phone',
        'image',
        'acc_creation_time',
        
    ]
    search_fields = ['user__username', 'email', 'phone']
    list_filter = ['gender', 'acc_type', 'country', 'acc_creation_time']

# Removing unnecessary import statements and comments for clarity



# admin.py

from django.contrib import admin
from miniaccounts.models import EmailVerification

class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'created_at')
    # Add any other configurations or customizations you want for the admin interface

admin.site.register(EmailVerification, EmailVerificationAdmin)
