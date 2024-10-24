import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def similarity(text:str, model:str, numword:int, return_json:bool):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}

    url = "https://api.aiforthai.in.th/thaiwordsim"

    if model != 'thwiki' and model != 'twitter':
        raise ValueError(
            f"""Model \"{model}\" not found."""
        )
    data = {'word':text,'model':model,'numword':str(numword)}
    
    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        return res.json()['words']
    else:
        return res.json()
