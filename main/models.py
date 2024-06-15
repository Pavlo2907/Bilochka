from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 2)  # Chief-Teacher

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, email, password, **extra_fields)

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractUser):
    ROLE_CHOICES = (
        ('teacher', 'Teacher'),
        ('chief_teacher', 'Chief Teacher'),
        ('student', 'Student'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')
    user_type = models.IntegerField(choices=((1, 'Teacher'), (2, 'Chief Teacher'), (3, 'Student')), default=3)
    objects = CustomUserManager()

class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Class(models.Model):  # Renamed from Class
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name

class Teacher(models.Model):
    # first_name = models.CharField(max_length=50, default='')  # Added default value for first_name
    # last_name = models.CharField(max_length=50, default='')  # Added default value for last_name
    username = models.CharField(max_length=50, default='Teacher')
    email = models.EmailField(default='example@email.com')  # Example default value for email
    # Add other fields if necessary

    def __str__(self):
        return f'{self.username}'

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject, related_name='students')
    achievements = models.TextField(blank=True, null=True)
    def calculate_average_grade(self):
        # Отримайте всі оцінки учня
        all_grades = self.grades.all()
        # Перевірте, чи є оцінки для розрахунку середньої
        if all_grades.exists():
            # Розрахунок середньої оцінки
            total_grades = sum([grade.grade for grade in all_grades])
            average_grade = total_grades / all_grades.count()
            return round(average_grade, 2)  # Округлення до двох знаків після коми
        else:
            return None

    def __str__(self):
        return self.user.username

class StudyMaterial(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='study_materials/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class Assignment(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(default=timezone.now)  # Added default value

    def __str__(self):
        return self.title

class Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateField(default=timezone.now)  # Set default to current date

    def __str__(self):
        return self.title

from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Grade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.student.user.username} - {self.subject.name} - {self.grade}'


class Schedule(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.subject} - {self.teacher} - {self.start_time} to {self.end_time}"
