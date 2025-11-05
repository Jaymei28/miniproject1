from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str__(self):
        return self.comment
    
class Department(models.Model):
    name = models.CharField(max_length=100)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
