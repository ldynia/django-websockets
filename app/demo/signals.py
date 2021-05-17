from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from demo.models import Person


@receiver(post_save, sender=Person)
def model_update(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('person', {
        'type': 'send.data',
        'data': {
            'message': 'Hello signals over WebSocket!'
        }
    })