from django.contrib import admin
from .models import MyUser, Course, Register, Event, Comment, Image, Material


class MyUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'first_name',
        'last_name',
        'email',
        'phone',
    )
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'email')


class CourseAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'short_description', 'amount', 'duration',
                    'level')
    list_display_links = ('id', 'title')
    prepopulated_fields = {"slug": ("title", )}


class RegisterAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'surname',
        'email',
        'phone',
        'course',
    )
    list_display_links = ('id', 'name')
    search_fields = ('phone', 'email')


class EventAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'short_description',
        'duration',
        'data',
        'speaker',
    )
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    prepopulated_fields = {"slug": ("title", )}


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text')


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'lesson_name', 'number', 'course')
    search_fields = ('course__title', )


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Register, RegisterAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Image)
