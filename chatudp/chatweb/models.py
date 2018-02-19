from uuid import uuid4
from django.db import models


class Room(models.Model):
    room_name = models.CharField(max_length=300)
    my_username = models.CharField(max_length=300)
    room_password = models.CharField(max_length=300)
    is_active = models.BooleanField()

    def __str__(self):
        return self.room_name


class Participant(models.Model):
    username = models.CharField(max_length=300)
    ip = models.CharField(max_length=46)
    is_online = models.BooleanField()
    last_activity = models.DateTimeField(auto_now=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class Message(models.Model):
    uuid = models.UUIDField(null=False, default=uuid4)
    datetime = models.DateTimeField(null=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
    refer_message = models.UUIDField(null=True)

    class Meta:
        abstract = True


class SentTextMessage(Message):
    is_sent = models.BooleanField()
    participants_received = models.ManyToManyField(Participant, related_name='+')
    participants_read = models.ManyToManyField(Participant, related_name='+')

    def __str__(self):
        return self.text


class ReceivedTextMessage(Message):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
