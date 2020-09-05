from django.db import models


class Institution(models.Model):
    type_choices = [
        ("1", "middle school"),
        ("2", "high school"),
        ("3", "college"),
        ("4", "bootcamp"),
        ("5", "other"),
    ]
    iID = models.CharField(max_length = 100, primary_key=True) # institution ID
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 20, choices=type_choices)

    def __unicode__(self):
        return self.name

# Create your models here.
class Course(models.Model):
    cID =  models.CharField(max_length = 100, primary_key=True) # course ID
    title = models.TextField()
    subject = models.TextField()
    iID = models.ForeignKey(Institution, on_delete=models.CASCADE)
