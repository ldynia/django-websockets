from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer


class ModelConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.model = self.scope['url_route']['kwargs']['model_name']

        async_to_sync(self.channel_layer.group_add)(self.model, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.model, self.channel_name)
        self.close()

    def receive_json(self, content):
        async_to_sync(self.channel_layer.group_send)(self.model, {
            'type': 'send.data',
            'data': content
        })

    def send_data(self, event):
        self.send_json(content=event['data'])
