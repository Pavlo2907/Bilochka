from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserLoginForm, SubjectForm, UserForm
from .models import Subject, Teacher, Class, User, StudentProfile
from django.contrib import messages

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
def teacher_subjects(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    return render(request, 'main/teacher_subjects.html', {'teacher': teacher})

from django.shortcuts import render, get_object_or_404
from .models import Teacher

def teacher_subject_detail(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    subjects = teacher.subjects.all()
    return render(request, 'main/teacher_subjects.html', {'teacher': teacher, 'subjects': subjects})


@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
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
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully.')
        return redirect('user_list')
    return render(request, 'main/user_confirm_delete.html', {'user': user})

@login_required
def statistics_view(request):
    # Your logic here
    return render(request, 'main/statistics.html')

@login_required
def teacher_subjects(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    return render(request, 'main/teacher_subjects.html', {'teacher': teacher})

@login_required
def subject_create_view(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')
    else:
        form = SubjectForm()
    return render(request, 'main/subject_create.html', {'form': form})

