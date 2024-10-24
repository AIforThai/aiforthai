import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def tokenize(text:str, return_json:bool):
    api_key = get_api_key()
    url = "https://api.aiforthai.in.th/tpos"
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    data = {'text':text}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['words']
    else:
        return res.json()
