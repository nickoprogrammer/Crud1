from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "status", "is_premium", "created_at", "deleted_at")

admin.site.register(Course, CourseAdmin)
