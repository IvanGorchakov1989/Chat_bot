import requests
import time
import thingspeak
from config import *
import json
    
offset = -2
counter = 0
chat_id: int

ch = thingspeak.Channel(id = channel_id_small_room, api_key = thingspeak_api_key)

temperature = round(float(json.loads(ch.get_field_last(field=1))['field1']), 2)
humidity = round(float(json.loads(ch.get_field_last(field=2))['field2']), 2)
battery_Voltage = round(float(json.loads(ch.get_field_last(field=3))['field3']), 2)
print(temperature, humidity, battery_Voltage)
# while counter < MAX_COUNTER:

#     print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

#     time.sleep(1)
#     counter += 1

# offset = -2
# counter = 0
# cat_response: requests.Response
# cat_link: str

# while counter < 100:
#     print('attempt =', counter)
#     updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

#     if updates['result']:
#         for result in updates['result']:
#             offset = result['update_id']
#             chat_id = result['message']['from']['id']
#             cat_response = requests.get(API_CATS_URL)
#             if cat_response.status_code == 200:
#                 cat_link = cat_response.json()[0]['url']
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
#             else:
#                 requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

#     time.sleep(1)
#     counter += 1