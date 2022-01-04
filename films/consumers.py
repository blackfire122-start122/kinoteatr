import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
import redis

# r = redis.StrictRedis(
#     host='localhost',
#     port=6379,
# )
# r.set("id",1,10)
# print(r.get("id"))

channel_layer = get_channel_layer()

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await channel_layer.send(self.channel_name, {
            "type": "send.sdp",
            "data": {'channel': self.channel_name},
        })
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        message = data_json.get('message')
        action = data_json.get('action')

        data_json['channel'] = self.channel_name
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'send.sdp',
                'data': data_json,
            }
        )

    async def send_sdp(self, event):
        receive = event['data']
        await self.send(text_data=json.dumps(receive))

    async def call_message(self, event):
        await self.send(text_data=json.dumps(event))