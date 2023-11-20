import json
import time
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

from .monitor import get_system_data

class ScreenTrackConsumer(WebsocketConsumer):
    '''Consumer for monitoring and getting screen time data from system'''
    
    def connect(self):
        '''Connect to websocket'''
        
        self.group_name = 'group'
        
        async_to_sync(self.channel_layer.group_add) (
            self.group_name,
            self.channel_name
        )
        
        self.accept()
        
        # send message over websocket
        self.send(text_data= json.dumps({
            'type': 'connection-check',
            'message': 'Connection Successful'
        }))
        
    def receive(self, text_data):
        '''
            Function to receive data
            This function will get system data from monitor.py file
        '''
        
        # Load data being sent to the consumer
        data = json.loads(text_data)
        cpu_percent = data.get('cpu_percent', None)
        
        async_to_sync(self.channel_layer.group_send) (
            self.group_name, {
                'type': 'fetch_system_data',
                'cpu_percent': cpu_percent
            }
        )
        
        # print(f'CPU Percent- {cpu_percent}')
        
        # Handle data gotten from monitor.py
        # self.send(text_data=json.dumps({
        #     'type': 'system-info-cpu',
        #     'cpu_percent': cpu_percent,
        # }))
        
    
    def fetch_system_data(self, event):
        '''Function to get system data'''
        
        while True:
            system_data = get_system_data()
            
            self.send(text_data=json.dumps({
                'cpu_percent': system_data['cpu_percent'],
                'cpu_count': system_data['cpu_count'],
            }))

            time.sleep(5)
            
        