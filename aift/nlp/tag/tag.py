import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(text:str, numtag:int=5, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = "https://api.aiforthai.in.th/tagsuggestion"   
    data = {'text':text,'numtag':str(numtag)}
        
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['tags']
    else:
        return res.json()
