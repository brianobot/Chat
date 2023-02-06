from django.db import models
from django.conf import settings

# Create your models here.
class ChatRoom(models.Model):
    room_id = models.CharField(max_length=100, unique=True, blank=True)
    member = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return str(self.room_id)

    def save(self, *args, **kwargs):
        if not self.room_id:
            import time
            self.room_id = time.time() 
        # Call the superclass save method
        super().save(*args, **kwargs)
        

class Message(models.Model):
    # TODO: refactor the user duplication in the message model since there are already present in the chat room model
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='recipient', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    chatroom = models.ForeignKey("ChatRoom", on_delete=models.SET_NULL, null=True, related_name="messages")

    def __str__(self):
        return f"TO: {self.receiver} FROM: {self.sender}"

    class Meta:
        ordering = ('created' ,)