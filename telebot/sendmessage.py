import requests
from .models import TeleSettings


def sendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        text = str(settings.tg_message)
        chat_id = str(settings.tg_chat)
        api = "https://api.telegram.org/bot"
        method = api + token + '/sendMessage'
        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            a = text.find('{')
            b = text.find('}')
            c = text.rfind('{')
            d = text.rfind('}')
            part1= text[0:a]
            part2= text[b+1:c]
            part3= text[d:-1]

            text_slice = part1 +tg_name+ part2+tg_phone + part3
        
        else: text_slice = text

        try:
            req = requests.post(method, data={
            "chat_id": chat_id,
            "text": text_slice})
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Sending Error!')
            elif req.status_code == 500:
                print('Server Error!')
            else:
                print('Success!')
            
    else:  
        pass
