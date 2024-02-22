from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length = 50, null = False)
    description = models.TextField(max_length = 255, blank = True, null = True)
    start_date = models.DateField()
    updated_at = models.DateField( auto_now = True)
    is_completed = models.BooleanField(default = False)


    def __str__(self):
        return self.title