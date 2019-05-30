# WS server that sends messages at random intervals
import asyncio
import datetime
import random
import logging
import websockets

response = {'click': [], 'e': []}

async def stim(websocket, path):
    for i in range(1, 4):
        stimulus_link = "stimulus/" + str(i) + ".jpg"
        await websocket.send(stimulus_link)
        print('sent stimulus')
        
        await asyncio.sleep(1)
        
        # process message sent from client
        async for message in websocket:
            data = json.loads(message)
            await response['click'].append(data['rt'])
        
        """
        async for message in websocket:
            data = json.loads(message)
            if data['action'] == 'click':
                response['click'].append(data['rt'])
            elif data['action'] == 'pressed e':
                response['e'].append(data['rt'])
            else:
                logging.error(
                    "unsupported event: {}", data)
        """
        #print(response)
        
        

start_server = websockets.serve(stim, '127.0.0.1', 8787)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
