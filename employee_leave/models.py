from django.db import models
from django.contrib.auth.models import User

LEAVE_TYPE = (
    ('sick', 'sick'),
    ('maternity', 'maternity'),
    ('dayoff', 'dayoff'),
    ('anually_leave', 'anually leave'),
    ('other', 'other'),
)

STATUS = (
    ('pending', 'pending'),
    ('cancelled', 'cancelled'),
    ('approved', 'approved'),
)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    sex = models.CharField(max_length=7, blank=True, null=True)
    salary = models.IntegerField()
    position = models.CharField(max_length=200)
    hire_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='profile/')

    def __str__(self):
        return str(self.user)


class Leave(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=30, choices=LEAVE_TYPE)
    leave_date = models.DateField()
    return_date = models.DateField()
    status = models.CharField(max_length=30, choices=STATUS, default='pending', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.employee} - {self.leave_date}'
