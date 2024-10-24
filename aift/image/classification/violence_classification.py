import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(file:str, return_json:bool=True):
    api_key = get_api_key()
    url = "https://api.aiforthai.in.th/violent"

    payload={}
    files=[('file',(file,open(file,'rb'),'image/jpeg'))]

    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    res = requests.request("POST", url, headers=headers, data=payload, files=files)

    if return_json == False:
        return res.json()['objects']
    else:
        return res.json()

