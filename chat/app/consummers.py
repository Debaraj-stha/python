import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync  import async_to_sync
import urllib.parse
class MyConummer(WebsocketConsumer):
    def connect(self):
        query_string = self.scope['query_string'].decode('utf-8')
        query_params = urllib.parse.parse_qs(query_string)
        groupName = query_params.get('group', [None])[0]
        userId = query_params.get('user_id', [None])[0]

        self.room_name= groupName if groupName is not None else userId
        self.room_group_name= 'group_%s' %groupName if groupName is not None else userId
        print("connection established")

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"payload": "this is a response from server"}))
        pass
    def disconnect(self, code):
        self.send({"type": "websocket.disconnect", "test": "disconnect "})
        return super().disconnect(code)
    def receive(self, text_data):
        print("received message: " + text_data)
        self.send(text_data=json.dumps({"message":"Message is received"}))
    def custom_message(self,event):
        print("custom message is called")
        eventType = event["type"]
        text_data = event["text"]
        print(f"event ${str(event)}")
        self.send(text_data=text_data)