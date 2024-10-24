import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def generate(file:str, instruction:str, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th/audioqa/inference/"

    payload = {'instruction': instruction}
    files=[('file',(file,open(file,'rb'),'audio/mpeg'))]
    res = requests.request("POST", url, data=payload, headers=headers, files=files)

    if return_json == False:
        return res.json()['content']
    else:
        return res.json()