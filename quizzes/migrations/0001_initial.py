# Generated by Django 5.1.5 on 2025-02-03 21:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('flashcard_id', models.AutoField(primary_key=True, serialize=False)),
                ('front_content', models.TextField()),
                ('back_content', models.TextField()),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.file')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('questions', models.JSONField()),
                ('answers', models.JSONField()),
                ('options', models.JSONField()),
                ('quiz_type', models.CharField(choices=[('MCQ', 'Multiple Choice'), ('True/False', 'True/False')], max_length=100)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='files.file')),
            ],
        ),
        migrations.CreateModel(
            name='QuizPerformance',
            fields=[
                ('quiz_performance_id', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('attempt_number', models.IntegerField()),
                ('date_taken', models.DateTimeField(auto_now_add=True)),
                ('quiz', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz')),
            ],
        ),
    ]
