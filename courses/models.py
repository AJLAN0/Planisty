from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    semester = models.ForeignKey('semesters.Semester', on_delete=models.CASCADE)
    study_preference = models.OneToOneField('StudyPreferences', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class StudyPreferences(models.Model):
    preferences_id = models.AutoField(primary_key=True)
    study_intensity = models.CharField(max_length=50, choices=[('Light', 'Light'), ('Medium', 'Medium'), ('Intensive', 'Intensive')])

    def __str__(self):
        return self.study_intensity
