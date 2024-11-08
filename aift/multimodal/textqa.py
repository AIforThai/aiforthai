import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def generate(instruction:str, 
    system_prompt:str="You are Pathumma LLM, created by NECTEC. Your are a helpful assistant.", 
    max_new_tokens:int=512,
    temperature:float=0.4,
    return_json:bool=True):

    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = 'https://api.aiforthai.in.th/textqa/completion'
    payload = {
        'instruction': instruction,
        'system_prompt': system_prompt,
        'max_new_tokens':max_new_tokens,
        'temperature': temperature,
        'return_json': return_json
    }

    res = requests.post(url, headers=headers, data=payload)
    if return_json == False:
        return res.json()['content']
    else:
        return res.json()

def chat(instruction:str, 
    sessionid:str,
    context:str="", 
    temperature:float=0.4,
    return_json:bool=True):

    api_key = get_api_key()
    headers = {'accept': 'application/json', 'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = 'https://api.aiforthai.in.th/pathumma-chat'
    payload = {
        'context': context,
        'prompt' : instruction,
        'sessionid' : sessionid,
        'temperature': temperature,
    }

    res = requests.post(url, headers=headers, data=payload)
    if return_json == False:
        return res.json()['response']
    else:
        return res.json()
