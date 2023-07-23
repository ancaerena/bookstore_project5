from django.contrib import admin
from .models import Subject, Comments

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'subject', 
    )
class SubjectAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'topic',
    )

admin.site.register(Subject, SubjectAdmin)
admin.site.register(Comments, CommentsAdmin)