from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'updated_at')
    search_fields = ('question', 'question_hi', 'question_bn')
    readonly_fields = ('created_at', 'updated_at')
    
    fieldsets = (
        ('English', {
            'fields': ('question', 'answer'),
        }),
        ('Hindi Translation', {
            'fields': ('question_hi', 'answer_hi'),
            'classes': ('collapse',),
        }),
        ('Bengali Translation', {
            'fields': ('question_bn', 'answer_bn'),
            'classes': ('collapse',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
