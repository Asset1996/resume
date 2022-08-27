"""
Admin page customize.
"""
from django.contrib import admin
from .models import WorkExperience, User, Education
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    """Custom UserAdmin class."""
    ordering = ["id"]
    list_display = ["id", "email", "name_en"]
    search_fields = ["email", "name_en"]
    empty_value_display = "--empty--"
    fieldsets = (
        (None, {
            "fields": (
                "email", "name_en", "name_ru", "surname_en", "surname_ru", 
                "password", "skills", "degree", "birthday", "phone", "instagram",
                "linkedin", "github", "experience", "address_en", "address_ru"
            ),
        }),
        ("Permissions", {
            "fields": (
                "is_staff", "is_active", "is_superuser",
            ),
        }),
        ("Dates", {
            "fields": (
                "last_login",
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": (
                "email", 
                "password1", 
                "password2", 
                "name_en", 
                "name_ru", 
                "surname_en", 
                "surname_ru",
                "is_active", 
                "is_staff", 
                "is_superuser", 
                "skills"
            ),
        }),
    )
    readonly_fields = ["last_login"]

class WorkExperienceAdmin(admin.ModelAdmin):
    """Custom WorkExperience models WorkExperienceAdmin class."""
    ordering = ["id"]
    list_display = ["user", "company_name_en", "position_en"]
    search_fields = ["user__email", "company_name_en", "position_en"]
    empty_value_display = "--empty--"

class EducationAdmin(admin.ModelAdmin):
    """Custom Education models EducationAdmin class."""
    ordering = ["id"]
    list_display = ["user", "institution_name_en", "speciality_en"]
    search_fields = ["user__email", "institution_name", "speciality"]
    empty_value_display = "--empty--"

admin.site.register(WorkExperience, WorkExperienceAdmin)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Education, EducationAdmin)
