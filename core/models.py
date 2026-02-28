from django.db import models

# Create your models here.
from django.db import models

class UserPreference(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    skill_level = models.CharField(max_length=50, null=True, blank=True)
    learning_goal = models.CharField(max_length=100, null=True, blank=True)
    prog_language = models.CharField(max_length=50, null=True, blank=True)
    study_time = models.CharField(max_length=50, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.email
        from django.db import models

# ... unga pazhaya models (User/Profile) inga irukkum ...

class UserActivity(models.Model):
    # Indha lines ellam class-ku kulla 'indent' aagi irukkanum (Press Tab)
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)
    task_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.email} completed {self.task_name} on {self.date}"