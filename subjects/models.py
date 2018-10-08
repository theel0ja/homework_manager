from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=50) # todo: might have to change max_length to soemthing better

    def __str__(self):
        return self.name