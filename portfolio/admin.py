from django.contrib import admin
from .models import Project, Skill, Profile, Contact


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "technologies",
        "created",
    )

    search_fields = (
        "title",
        "technologies",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )
    
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "title",
    )
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "subject",
        "sent_at",
    )

    search_fields = (
        "name",
        "email",
        "subject",
    )

    list_filter = (
        "sent_at",
    )