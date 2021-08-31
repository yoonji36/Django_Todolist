from django.db import models

class Todolist(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.content