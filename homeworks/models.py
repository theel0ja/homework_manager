from django.db import models

# Create your models here.

class Homework(models.Model):
    description = models.CharField(max_length=150) # todo: might have to change max_length to soemthing better

    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)

    due_date = models.DateTimeField()