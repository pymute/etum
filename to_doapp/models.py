from django.db import models
from datetime import datetime
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class TodoModel(models.Model):
    task_name = models.CharField(default='',max_length=25)
    task_desc = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    update_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(User,default='',on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.task_name


    class Meta:
        db_table = 'todo'
        