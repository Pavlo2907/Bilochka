# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, SubjectForm, UserForm, StudyMaterialForm, AssignmentForm, AchievementForm
from .models import Subject, Teacher, Class, User, StudentProfile, StudyMaterial, Assignment, Achievement

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    subjects = Subject.objects.all()
    teachers = Teacher.objects.all()
    num_classes = Class.objects.count()
    num_students = StudentProfile.objects.count()

    context = {
        'subjects': subjects,
        'teachers': teachers,
        'num_classes': num_classes,
        'num_students': num_students,
    }

    return render(request, 'main/home.html', context)

@login_required
def teacher_list(request):
    teachers = Teacher.objects.all().order_by('last_name')
    return render(request, 'main/teacher_list.html', {'teachers': teachers})

@login_required
def subject_create(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'main/subject_form.html', {'form': form})

@login_required
def subject_list(request):
    subjects = Subject.objects.all().order_by('name')
    return render(request, 'main/subject_list.html', {'subjects': subjects})

@login_required
def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        form = SubjectForm(request.POST, instance=subject)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm(instance=subject)
    return render(request, 'main/subject_form.html', {'form': form})

@login_required
def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject.delete()
        return redirect('subject_list')
    return render(request, 'main/subject_confirm_delete.html', {'subject': subject})

@login_required
def user_list(request):
    users = User.objects.order_by('username')
    return render(request, 'main/user_list.html', {'users': users})

@login_required
def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'main/user_form.html', {'form': form})

@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'main/user_form.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'main/user_confirm_delete.html', {'user': user})

@login_required
def statistics_view(request):
    # Implement statistics logic
    return render(request, 'main/statistics.html')

@login_required
def study_material_list(request):
    materials = StudyMaterial.objects.all()
    return render(request, 'main/study_material_list.html', {'materials': materials})


@login_required
def study_material_create(request):
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('study_material_list')
    else:
        form = StudyMaterialForm()
    return render(request, 'main/study_material_form.html', {'form': form})


@login_required
def study_material_update(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect('study_material_list')
    else:
        form = StudyMaterialForm(instance=material)
    return render(request, 'main/study_material_form.html', {'form': form})

@login_required
def study_material_delete(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    if request.method == 'POST':
        material.delete()
        return redirect('study_material_list')
    return render(request, 'main/study_material_confirm_delete.html', {'material': material})

@login_required
def assignment_list(request):
    assignments = Assignment.objects.all().order_by('title')
    return render(request, 'main/assignment_list.html', {'assignments': assignments})

@login_required
def assignment_create(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm()
    return render(request, 'main/assignment_form.html', {'form': form})

@login_required
def assignment_update(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, instance=assignment)
        if form.is_valid():
            form.save()
            return redirect('assignment_list')
    else:
        form = AssignmentForm(instance=assignment)
    return render(request, 'main/assignment_form.html', {'form': form})

@login_required
def assignment_delete(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method == 'POST':
        assignment.delete()
        return redirect('assignment_list')
    return render(request, 'main/assignment_confirm_delete.html', {'assignment': assignment})

@login_required
def achievement_list(request):
    achievements = Achievement.objects.all().order_by('title')
    return render(request, 'main/achievement_list.html', {'achievements': achievements})

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AchievementForm
from .models import Achievement

@login_required
def achievement_create(request):
    if request.method == 'POST':
        form = AchievementForm(request.POST)
        if form.is_valid():
            achievement = form.save(commit=False)
            achievement.user = request.user  # Assign the current logged-in user
            achievement.save()
            return redirect('achievement_list')
    else:
        form = AchievementForm()
    return render(request, 'main/achievement_form.html', {'form': form})


@login_required
def achievement_update(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        form = AchievementForm(request.POST, instance=achievement)
        if form.is_valid():
            form.save()
            return redirect('achievement_list')
    else:
        form = AchievementForm(instance=achievement)
    return render(request, 'main/achievement_form.html', {'form': form})

@login_required
def achievement_delete(request, pk):
    achievement = get_object_or_404(Achievement, pk=pk)
    if request.method == 'POST':
        achievement.delete()
        return redirect('achievement_list')
    return render(request, 'main/achievement_confirm_delete.html', {'achievement': achievement})

@login_required
def profile(request):
    return render(request, 'main/profile.html')

@login_required
def profile_update(request):
    # Implement profile update logic
    return render(request, 'main/profile_update.html')

@login_required
def profile_delete(request):
    # Implement profile delete logic
    return render(request, 'main/profile_delete.html')