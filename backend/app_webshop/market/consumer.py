from channels.generic.websocket import WebsocketConsumer
from channels.consumer import AsyncConsumer, SyncConsumer
import json

class MarketConsumer(SyncConsumer):
    groups = ["broadcast"]

    def websocket_connect(self, event):
        # Called on connection.
        # To accept the connection call:
        self.send({
            "type": "websocket.accept"
        })
        self.send({
            'type': 'websocket.send',
            'text_data': 'this message from server!'
        })
        # Or accept the connection and specify a chosen subprotocol.
        # A list of subprotocols specified by the connecting client
        # will be available in self.scope['subprotocols']
        # self.accept("subprotocol")
        # To reject the connection, call:
        # self.close()

    def websocket_receive(self, event=None, bytes_data=None):
        print(event["text"])
        self.send({
            "type": "websocket.send",
            "text": event["text"]
        })
        # message = text_data_json['message']
        # self.send(text_data=json.dumps({
        #     'message': message
        # }))
        # You can call:
        # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # Want to force-close the connection? Call:
        # self.close()
        # Or add a custom WebSocket error code!
        # self.close(code=4123)

    async def websocket_disconnect(self, close_code):
        pass
        # Called when the socket closes