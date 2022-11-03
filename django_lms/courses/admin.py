from django.contrib import admin

from .models import Course


class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'duration', 'price')
    list_display_links = list_display
    list_per_page = 15
    list_filter = ('course_name',)
    fields = [
             ('course_name', ),
             ('duration', 'price'),
             'description',
             'group',
         ]


admin.site.register(Course, CourseAdmin)
