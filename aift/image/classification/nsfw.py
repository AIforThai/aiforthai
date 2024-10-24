import requests,json,base64 
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(file:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'Content-Type':'application/json', 'X-lib':PACKAGE_NAME}
    fileByte = open(file, 'rb').read()
    b64 = base64.b64encode(fileByte)
    params = json.dumps({"file":b64.decode('ascii') })

    url ='https://api.aiforthai.in.th/nsfw'

    
    res = requests.post(url, data=params, headers=headers)
    
    if return_json == False:
        return res.json()['objects']
    else:
        return res.json()

