from django.contrib import admin
from .models import Room, Participant, SentTextMessage, ReceivedTextMessage


class RoomAdmin(admin.ModelAdmin):
    pass


class ParticipantAdmin(admin.ModelAdmin):
    pass


class SentTextMessageAdmin(admin.ModelAdmin):
    pass


class ReceivedTextMessageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Room, RoomAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(SentTextMessage, SentTextMessageAdmin)
admin.site.register(ReceivedTextMessage, ReceivedTextMessageAdmin)
