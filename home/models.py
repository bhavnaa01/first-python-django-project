from django.db import models # type: ignore
from email.headerregistry import Address
from enum import _auto_null
from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore
class Student(models.Model):
    user=models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,default=None)
    mob=models.CharField(max_length=11)
    address=models.CharField(max_length=20)
    course=models.CharField(max_length=20)
    edt=models.DateField(auto_now=False)
    remarks=models.CharField(max_length=100,default=None)
    def __str__(self) -> str:
        return self.course
class Joined(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    joined_dt=models.DateField(auto_now=False)
    total=models.IntegerField()
    first_ins=models.IntegerField()
    first_dt=models.DateField(auto_now=False)
    second_ins=models.IntegerField()
    second_dt=models.DateField(auto_now=False)
    duration=models.CharField(max_length=20)
    dues=models.IntegerField(default=0)
    def __str__(self) -> str:
        return str(self.second_dt.strftime("%Y-%m-%d"))
class Batch(models.Model):
    student=models.ManyToManyField(Joined)
    start_dt=models.DateField(auto_now=False)
    trainer=models.CharField(max_length=20)
    bname=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.bname
class Trainer(models.Model):
    tname=models.CharField(max_length=20)
    languages=models.CharField(max_length=30)
    sal=models.IntegerField()
    joined_dt=models.DateField(auto_now=False)
    timinings=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.tname 

