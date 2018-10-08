from django.db import models

# Create your models here.

class Homework(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    description = models.CharField(max_length=150) # todo: might have to change max_length to soemthing better

    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE)

    due_date = models.DateTimeField()


    def __str__(self):
        return "{} ({})".format(self.description, self.subject)