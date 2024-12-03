import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def generate(instruction:str, 
    max_new_tokens:int=1024,
    temperature:float=0.0,
    return_json:bool=True):

    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = 'https://api.aiforthai.in.th/word-correction/completion'
    payload = {
        'instruction': instruction,
        'max_new_tokens':max_new_tokens,
        'temperature': temperature,
        'return_json': return_json
    }

    res = requests.post(url, headers=headers, data=payload)
    if return_json == False:
        return res.json()['content']
    else:
        return res.json()
