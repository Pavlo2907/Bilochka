# Generated by Django 5.0.6 on 2024-06-15 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_teacher_first_name_remove_teacher_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='user_name',
            new_name='username',
        ),
    ]
