from django.contrib import admin

from .models import Profile, Organization, Membership, Project, Team, TeamRole


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'slug')
    list_filter = ('user',)
    search_fields = ('slug',)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uuid', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'organization', 'uuid')
    list_filter = ('profile', 'organization')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'organization')
    list_filter = ('organization',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'organization')
    list_filter = ('organization',)
    raw_id_fields = ('members',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ['name']}


@admin.register(TeamRole)
class TeamRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uuid', 'team', 'project', 'role_type')
    list_filter = ('team', 'project')
    search_fields = ('name',)
