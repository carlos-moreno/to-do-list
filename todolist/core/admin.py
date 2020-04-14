from django.contrib import admin

from todolist.core.models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'ended']
    list_display = ['title', 'description', 'ended']


admin.site.register(ToDo, ToDoAdmin)
