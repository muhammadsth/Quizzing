from django.db import models


class Institution(models.Model):
    type_choices = [
        ("1", "middle school"),
        ("2", "high school"),
        ("3", "college"),
        ("4", "bootcamp"),
        ("5", "other"),
    ]
    iID = models.AutoField(primary_key=True) # institution ID
    name = models.CharField(max_length = 100)
    type = models.CharField(max_length = 20, choices=type_choices)

    def __unicode__(self):
        return self.name

    class Meta:
        unique_together = ('name', 'type',)

# Create your models here.
class Course(models.Model):
    cID = models.AutoField(primary_key=True) # course ID
    code = models.CharField(max_length=10)
    title = models.TextField()
    subject = models.TextField()
    iID = models.ForeignKey(Institution, on_delete=models.CASCADE)
    studied_by = models.ManyToManyField('pages.Profile')

    class Meta:
        unique_together = ('code', 'title', 'subject',)
