from django.contrib import admin

from .models import Profile, Organization, Membership, Project, Team, TeamRole, TeamAssignment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'id', 'slug')
    list_filter = ('user',)
    search_fields = ('slug',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'uuid', 'slug', 'personal')
    search_fields = ('name',)


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('profile', 'id', 'organization', 'uuid')
    list_filter = ('organization',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'organization')
    list_filter = ('organization',)
    search_fields = ('name',)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'organization')
    list_filter = ('organization',)
    search_fields = ('name',)


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'uuid')
    search_fields = ('name',)


@admin.register(TeamAssignment)
class TeamAssignmentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'uuid', 'team', 'project')
    list_filter = ('team', 'project')
