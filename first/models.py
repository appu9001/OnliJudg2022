
from django.db import models

# Create your models here.
class Problems(models.Model):
    statement=models.CharField(max_length=200)
    Name=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    Difficulty=models.CharField(max_length=200)

class Solutions(models.Model):
    problem=models.ForeignKey(Problems,on_delete=models.CASCADE)
    verdict=models.CharField(max_length=200)
    submission=models.DateTimeField()


class TestCases(models.Model):
        Input=models.CharField(max_length=200)
        Output=models.CharField(max_length=200)
        question=models.ForeignKey(Problems,on_delete=models.CASCADE)








        



