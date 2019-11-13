from django.contrib import admin
from .models import Category, Department, Log, Status, Task, User

admin.site.register(Category)
admin.site.register(Department)
admin.site.register(Log)
admin.site.register(Status)
admin.site.register(User)
admin.site.register(Task)
