from django.db import models

# Create your models here.
class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user.username}"
