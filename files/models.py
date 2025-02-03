from django.db import models

# Create your models here.
class File(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    file_path = models.CharField(max_length=255)
    course = models.ForeignKey('courses.Course', on_delete=models.CASCADE)

    def __str__(self):
        return self.file_name
