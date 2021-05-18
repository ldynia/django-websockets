from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class ModelConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.model = self.scope['url_route']['kwargs']['model_name']

        await self.channel_layer.group_add(self.model, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.model, self.channel_name)
        await self.close()

    async def receive_json(self, content):
        await self.channel_layer.group_send(self.model, {
            'type': 'send.data',
            'data': content
        })

    async def send_data(self, event):
        await self.send_json(content=event['data'])
