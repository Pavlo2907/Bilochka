from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .models import User, Subject, Class, StudentProfile, Teacher, Achievement, Assignment, StudyMaterial

# Створюємо клас UserAdmin
class UserAdmin(BaseUserAdmin):
    # Поля, які будуть відображатися в адмінці
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Role info', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Реєструємо нашу модель та наш UserAdmin клас
admin.site.register(User, UserAdmin)

# Реєструємо інші моделі
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(StudentProfile)
admin.site.register(Teacher)

# Видаляємо стандартну групу
admin.site.unregister(Group)
admin.site.register(Achievement)
admin.site.register(Assignment)
admin.site.register(StudyMaterial)