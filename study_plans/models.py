from django.db import models

# Create your models here.
class StudyPlan(models.Model):
    study_plan_id = models.AutoField(primary_key=True)
    course = models.OneToOneField('courses.Course', on_delete=models.CASCADE)
    progress_status = models.CharField(max_length=100, choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Completed', 'Completed')])
    course_schedule = models.JSONField()

    def __str__(self):
        return f"Study Plan for {self.course.title}"

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    study_plan = models.ForeignKey(StudyPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    due_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return self.title
