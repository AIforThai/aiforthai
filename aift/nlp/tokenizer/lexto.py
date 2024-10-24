import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def tokenize(text:str, normalize:bool, return_json:bool):
    api_key = get_api_key()
    url ='https://api.aiforthai.in.th/lextoplus'
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    data = {'text':text}
    
    if normalize == False:
        data['norm'] = '0'
    else:
        data['norm'] = '1'
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['tokens']
    else:
        return res.json()
