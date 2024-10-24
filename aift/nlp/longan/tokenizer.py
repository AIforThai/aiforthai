import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def tokenize(text:str, wordseg:bool=True, sentseg:bool=True, sep:str='|', return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = 'https://api.aiforthai.in.th/longan/tokenize'
    payload = {'text':text, 'wordseg':wordseg, 'sentseg': sentseg, 'sep': sep}

    res = requests.post(url, data=payload, headers=headers)

    if return_json == False:
        return res.json()['result']
    else:
        return res.json()