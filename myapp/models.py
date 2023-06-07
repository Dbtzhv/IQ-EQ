from django.db import models

class Test(models.Model):
    login = models.CharField(max_length=10, unique=True)

class IQTestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    score = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

class EQTestResult(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    letters = models.CharField(max_length=5)
    timestamp = models.DateTimeField(auto_now_add=True)