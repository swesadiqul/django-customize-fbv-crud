from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        # verbose_name = "Contact"
        # verbose_name_plural = "Contacts"
        pass


class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='services/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " -----------> "+ f"{self.created_at}"
    
    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"
        
        
class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    status = models.BooleanField()
    
    def __str__(self):
        return self.title
