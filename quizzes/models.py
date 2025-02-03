from django.db import models

# Create your models here.
class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    file = models.ForeignKey('files.File', on_delete=models.CASCADE)
    questions = models.JSONField()
    answers = models.JSONField()
    options = models.JSONField()
    quiz_type = models.CharField(max_length=100, choices=[('MCQ', 'Multiple Choice'), ('True/False', 'True/False')])

    def __str__(self):
        return f"Quiz for {self.file.file_name}"

class Flashcard(models.Model):
    flashcard_id = models.AutoField(primary_key=True)
    file = models.ForeignKey('files.File', on_delete=models.CASCADE)
    front_content = models.TextField()
    back_content = models.TextField()

    def __str__(self):
        return f"Flashcard for {self.file.file_name}"

class QuizPerformance(models.Model):
    quiz_performance_id = models.AutoField(primary_key=True)
    quiz = models.OneToOneField(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    attempt_number = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Performance for {self.quiz.quiz_id}"
