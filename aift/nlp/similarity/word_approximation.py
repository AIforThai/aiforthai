import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def word_approx(text:str, model:str, return_json:bool):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = "https://api.aiforthai.in.th/wordapprox"
    data = {'word':text, 'model':model}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        if len(res.json()) == 0:
            return ''
        return res.json()['words']
    else:
        return res.json()
