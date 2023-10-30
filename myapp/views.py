from django.shortcuts import render, redirect
from myapp.forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'index.html')


def contact(request):
    #body
    return render(request, 'contact.html')


def feedback(request):
    form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def portfolio(request):
    #body
    return render(request, 'about.html')


def service(request):
    #body
    return render(request, 'service.html')


def create_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', False)
        
        if status == "on":
            status = True
        else:
            status = False    
        Task.objects.create(title=title, description=description, status=status)
        return redirect('task-list')
      
    return render(request, 'task/create-task.html')


def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task/task-list.html', {'tasks': tasks})



#status field doesn't update properly
def update_task(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status', False)
        if status == "on":
            status = True
        else:
            status = False
        Task.objects.update(title=title, description=description, status=status)
        return redirect('task-list')
    return render(request, 'task/update-task.html', {'task': task})


def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('task-list')





