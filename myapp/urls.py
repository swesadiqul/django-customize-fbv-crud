from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    
    
    #create task url here
    path('create-task/', views.create_task, name='create-task'),
    path('task-list/', views.task_list, name='task-list'),
    path('update-task/<int:id>/', views.update_task, name='update-task'),
    path('delete-task/<int:id>/', views.delete_task, name='delete-task'),
]
