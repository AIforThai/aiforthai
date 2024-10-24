import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(text:str, mode:str='ta', return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = 'https://api.aiforthai.in.th/vaja'
    params = {'text':text, 'mode':mode}

    res = requests.get(url, params=params, headers=headers)
    if return_json == False:
        return res.json()['output']
    else:
        return res.json()
