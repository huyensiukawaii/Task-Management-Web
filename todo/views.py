from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from .forms import CreateUserForm, LoginForm, CreateTaskForm, UpdateUserForm, UpdateProfileForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from .models import Task, Profile

# - import Django message notification

from django.contrib import messages




def home(request):

   return render(request, 'index.html')

# - Registering / Creating a user

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':

        form = CreateUserForm(request.POST)

        if form.is_valid():
            
            current_user = form.save(commit=False)

            form.save()


            profile = Profile.objects.create(user=current_user)


            messages.success(request, "User registration was successful!")

            return redirect('my_login')
    
    context = {'form': form}

    return render(request, 'register.html', context=context)



# -Login a user
def my_login(request):
    form = LoginForm

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)

            if user is not None:
                auth.login(request, user)

                return redirect("dashboard")

    context = {'form': form}

    return render(request, 'my_login.html', context = context)



# -Dashboard
@login_required(login_url='my_login')   #security layer, prove have an account first then access to dashboard

def dashboard(request):
   
    profile_pic = Profile.objects.get(user = request.user)

    context = {'profile': profile_pic}
    
    
    return render(request, 'profile/dashboard.html', context = context)




# -Profile management
@login_required(login_url='my_login')   #security layer, prove have an account first then access to dashboard

def profile_management(request):


    user_form = UpdateUserForm(instance=request.user)

    profile = Profile.objects.get(user = request.user)


    form_2 = UpdateProfileForm(instance=profile)


    if request.method == 'POST':
       
        user_form = UpdateUserForm(request.POST, instance=request.user)


        form_2 = UpdateProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid():
           
            user_form.save()

            return redirect("dashboard")

        if form_2.is_valid():

            form_2.save()

            return redirect("dashboard")


 
    user_form = UpdateUserForm(instance=request.user)    #Showing current user form

    context ={'user_form': user_form, 'form_2': form_2 }

    return render(request, 'profile/profile_management.html', context = context)


@login_required(login_url='my_login')
def deleteAccount(request):

    if request.method == 'POST':

        deleteUser = User.objects.get(username=request.user)

        deleteUser.delete()

        return redirect("")
    
    
    return render(request, 'profile/delete_account.html')









# -Create a task page
@login_required(login_url='my_login')

def createTask(request):

    form = CreateTaskForm()

    if request.method == 'POST':

        form = CreateTaskForm(request.POST)
    
        if form.is_valid():

            task = form.save(commit=False)

            task.user = request.user

            task.save()

            return redirect('view_tasks')
    
    context = {'form': form}

    return render(request, 'profile/create_task.html', context = context)



# -View all tasks page
"""
@login_required(login_url='my_login')
def viewTask(request):

    current_user = request.user.id

    task = Task.objects.all().filter(user=current_user)

    context = {'task': task}

    return render(request, 'profile/view_tasks.html', context = context)
"""

@login_required(login_url='my_login')
def viewTask(request):
    current_user = request.user.id
    tasks = Task.objects.filter(user=current_user)

    priority = request.GET.get('priority')
    if priority:
        tasks = tasks.filter(priority=priority)

    context = {'tasks': tasks, 'selected_priority': priority if priority else ''}
    return render(request, 'profile/view_tasks.html', context)

   
# -Update task page
@login_required(login_url='my_login')
def updateTask(request, pk):

    task = Task.objects.get(id=pk)

    form = CreateTaskForm(instance=task)

    if request.method == 'POST':
        form = CreateTaskForm(request.POST, instance = task)

        if form.is_valid:
            
            form.save()
            
            return redirect('view_tasks')
        
    context = {'form': form}

    return render(request, 'profile/update_task.html', context = context)



# -Delete task page

def deleteTask(request, pk):
    
    task = Task.objects.get(id = pk)

    if request.method == 'POST':

        task.delete()

        return redirect('view_tasks')
    
    return render(request, 'profile/delete_task.html')


# -Logout a user

def user_logout(request):
    
    auth.logout(request)
    
    return redirect("")
    
    















    
    















