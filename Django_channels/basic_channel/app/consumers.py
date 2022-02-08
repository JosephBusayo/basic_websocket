#consumers.py is quite similar to views.py in a regular django set up. But its used only in websocket
import json
from random import randint
from time import sleep

from channels.generic.websocket import WebsocketConsumer


class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        
        for i in range(10):
            self.send(json.dumps({'message': randint(0, 101)}))
            sleep(3)