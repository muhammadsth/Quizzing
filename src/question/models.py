from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    qID = models.CharField(max_length=100, primary_key=True)
    text = models.TextField()

    class Difficulty(models.IntegerChoices):
        EASY = 1
        MEDIUM = 2
        HARD = 3
        CHALLENGING = 4

    difficulty = models.IntegerField(choices=Difficulty.choices)
    answer = models.TextField()
    cID = models.ForeignKey('course.Course', on_delete=models.CASCADE)

class Grade(models.Model):
    qID = models.ForeignKey(Question, on_delete=models.CASCADE)
    cID = models.ForeignKey('course.Course', on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    num_asked = models.IntegerField(default=0)
    num_mistakes = models.IntegerField(default=0)
