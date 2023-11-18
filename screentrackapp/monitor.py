import psutil
import websockets
import time
import json
import asyncio

def get_system_data():
    '''Function to get crucial system data about processes running'''
    
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # Format data collected from the system
    data = {
        'cpu_percent': cpu_percent,
        'cpu_count': cpu_count,
    }
    
    return data

async def send_data_to_server(data):
    '''Function to send gotten data to server'''
    
    # Connect to websocket server
    uri = 'ws://localhost:3100/ws/screentime/'
    async with websockets.connect(uri=uri) as websocket:
        # Send data to server
        await websocket.send(json.dumps(data))
        await websocket.close()
        
if __name__ == '__main__':
    while True:
        try:
            # Get system data
            system_data = get_system_data()
            print('Connection to server successful. Transmitting data.')
            print(system_data)
            asyncio.get_event_loop().run_until_complete(send_data_to_server(system_data))
            
            time.sleep(5)
        except ConnectionRefusedError:
            print('''
                  Connection Refused. 
                  Couldn\'t contact the server. Please connect to the server.
                ''')