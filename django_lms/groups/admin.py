from django.contrib import admin

from groups.models import Group

from rangefilter.filters import DateRangeFilter


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_description', 'group_start_date', )
    list_display_links = list_display
    list_filter = (('group_start_date', DateRangeFilter), 'group_name',)
    fieldsets = (
        ('Information', {'fields': ('group_name',)}),
        ('Dates', {'fields': ('group_start_date', 'group_end_date')}),
        ('Teachers and Headman', {'fields': ('teachers', 'headman')}),
        ('Description', {'fields': ('group_description',)}),
    )


admin.site.register(Group, GroupAdmin)
