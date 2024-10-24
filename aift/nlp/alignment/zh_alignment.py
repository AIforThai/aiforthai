import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(zh_text:str, th_text:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = "https://api.aiforthai.in.th/zh-th-align"
    payload = json.dumps({"ZH": zh_text, "TH": th_text})

    res = requests.post(url, data=payload, headers=headers)

    if return_json == False:
        return res.json()['forward']
    else:
        return res.json()
