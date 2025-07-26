from django.contrib import admin
from .models import ContactMessage, EmailFromFooter

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "subject", "created_at")
    search_fields = ("first_name", "last_name", "email", "subject", "message")
    list_filter = ("subject", "created_at")

@admin.register(EmailFromFooter)
class EmailFooterAdmin(admin.ModelAdmin):
    list_display = ("email",)