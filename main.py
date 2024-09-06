import requests
import time
import thingspeak
from config import *
import json
import secrets

offset = -2
counter = 0
chat_id: int

ch = thingspeak.Channel(id = channel_id_small_room, api_key = thingspeak_api_key)

while counter < MAX_COUNTER:

    print('attempt =', counter)  #Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            result_text = result['message']['text'][1:]
            match result_text:
                case 'password':
                    text = secrets.token_urlsafe(20)
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
                case 'value':
                    temperature = round(float(json.loads(ch.get_field_last(field=1))['field1']), 1)
                    humidity = round(float(json.loads(ch.get_field_last(field=2))['field2']), 1)
                    battery_Voltage = round(float(json.loads(ch.get_field_last(field=3))['field3']), 1)
                    text = 'В маленькой комнате сейчас ' + str(temperature) + '*C, влажность ' + str(humidity) + '%, вольтаж батареи ' + str(battery_Voltage) + 'V'
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={text}')
                case 'graphs':
                    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')

    time.sleep(1)
    counter += 1

### Ниже код генерации картинки с котиком на любой запрос
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