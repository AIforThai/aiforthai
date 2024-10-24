import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(en_text:str, th_text:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = "https://api.aiforthai.in.th/en-th-align"
    payload = json.dumps({"EN": en_text, "TH": th_text})

    res = requests.post(url, data=payload, headers=headers)

    if return_json == False:
        return res.json()['forward']
    else:
        return res.json()
