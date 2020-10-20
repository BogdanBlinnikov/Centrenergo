from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User, Department, Division

admin.site.register(User, UserAdmin)
admin.site.register(Department)
admin.site.register(Division)