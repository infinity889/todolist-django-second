from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Info(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=100, unique=True)
    email = models.EmailField(blank=True, null = True) 

    def __str__(self):
        return self.username
    

class Team(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
    
    
