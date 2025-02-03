from django.db import models

# Create your models here.
class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
