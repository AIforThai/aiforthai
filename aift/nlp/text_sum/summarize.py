import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def summarize(text:str, comp_rate:float=30, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'Content-Type':'application/json', 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th/textsummarize"
    data = json.dumps([{"id":100,"comp_rate":comp_rate,"src":text}])

    res = requests.post(url, data=data, headers=headers)
    return res.json()