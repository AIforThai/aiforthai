import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(text:str, lim:int=1, minscore:float=0.1, return_json:bool=True):
    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th//ptt-qsearch/predict"
    params = {'text':text, "lim":lim,"minscore":minscore}

    res = requests.get(url, params=params, headers=headers)
    if return_json == False:
        return res.json()['predict']
    else:
        return res.json()
