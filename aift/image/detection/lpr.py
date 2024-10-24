import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(file:str, crop:str='0', rotate:str='1', return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th/lpr-v2"
    payload = {'crop': str(crop), 'rotate': str(rotate)}
    files = {'image':open(file, 'rb')}

    res = requests.post( url, files=files, data = payload, headers=headers)
    
    if return_json == False:
        return res.json()[0]['bbox']
    else:
        return res.json()

