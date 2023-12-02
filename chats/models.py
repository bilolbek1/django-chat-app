from django.db import models

from users.models import CustomUser

MESSAGES_TYPE = (
    ('sended', 'sended'),
    ('sending', 'sending')
)


class Messages(models.Model):
    text = models.CharField(max_length=200)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender', null=True)
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recipient', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    send_status = models.CharField(max_length=10, choices=MESSAGES_TYPE, default='sending')


    def __str__(self):
        return self.text[0:15]


























