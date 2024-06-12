from django.contrib import admin
from .models import User, Subject, Class, StudentProfile, Teacher, CustomUserManager
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

admin.site.register(User, UserAdmin)


admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(StudentProfile)
admin.site.register(Teacher)