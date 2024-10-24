import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def translate(text:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'Content-Type':'application/json', 'X-lib':PACKAGE_NAME}

    url = 'https://api.aiforthai.in.th/xiaofan-en-th/th2en'
    data = json.dumps({"text": text})
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['translated_text']
    else:
        return res.json()
