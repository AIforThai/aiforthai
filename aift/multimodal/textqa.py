import requests
import json
from aift.setting.setting import get_api_key, PACKAGE_NAME

def generate(instruction:str, 
    system_prompt:str="You are Pathumma LLM, created by NECTEC. Your are a helpful assistant.", 
    stop_tokens=["</s>", "<end_of_turn>"],
    max_new_tokens:int=256,
    temperature:float=0.4,
    return_json:bool=True):

    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME, 'Content-Type': 'application/json'}
    url = 'https://api.aiforthai.in.th/textqa/completion'
    payload = {
        'instruction': instruction,
        'system_prompt': system_prompt,
        'max_new_tokens':max_new_tokens,
        'temperature': temperature,
        'return_json': return_json
    }

    res = requests.post(url, headers=headers, data=payload)
    # response.json()
    # payload = json.dumps({
    #     "prompt": f"<|im_start|>system\n{system_prompt}<|im_end|>\n<|im_start|>user\n{instruction}<|im_end|>\n<|im_start|>assistant\n",
    #     "max_new_tokens": max_new_tokens,
    #     "temperature": temperature,
    #     "stop": stop_tokens})

    # res = requests.request("POST", url, data=payload, headers=headers)
    if return_json == False:
        return res.json()['content']
    else:

        return res.json()