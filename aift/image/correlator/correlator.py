import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(file:str, arr:str='คน', num:int=1, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th/sme-image-search/search"
    payload = {'arr': str(arr),'num': str(num)}
    files=[('image',(file,open(file,'rb'),'image/jpeg'))]
    
    res = requests.request("POST", url, headers=headers, data=payload, files=files)
    
    if return_json == False:
        return res.json()['objects']
    else:
        return res.json()

