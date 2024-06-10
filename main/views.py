from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import Subject, User



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
    subjects = Subject.objects.values('name').distinct().order_by('name')
    teachers = User.objects.filter(user_type=1).order_by('last_name')
    students = User.objects.filter(user_type=3)
    num_classes = subjects.count()
    num_students = students.count()
    return render(request, 'home.html', {
        'subjects': subjects,
        'teachers': teachers,
        'num_classes': num_classes,
        'num_students': num_students,
    })

