from django.contrib import admin
from .models import TodoModel
class TodoAmin(admin.ModelAdmin):
    list_display=('task_name','task_desc','created_at','user')
    search_fields= ('task_name','task_desc')


admin.site.register(TodoModel,TodoAmin)