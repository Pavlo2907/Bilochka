from django.contrib import admin
from .models import User, Subject, Class, StudentProfile, Teacher, CustomUserManager

admin.site.register(User)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(StudentProfile)
admin.site.register(Teacher)