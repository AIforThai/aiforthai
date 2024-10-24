import requests
from aift.setting.setting import get_api_key, PACKAGE_NAME

def analyze(text:str, return_json:bool):
    map_classes = {
        0: 'ข้อความทั่วไปซึ่งไม่มีลักษณะของการรังแก',
        1: 'ข้อความที่มีการกล่าวถึงบุคลิก รูปลักษณ์ และ พฤติกรรม',
        2: 'ข้อความที่เป็นคำด่า คำหยาบคาย',
        3: 'ข้อความคุกคามเกี่ยวกับทางเพศ',
        4: 'ข้อความที่กล่าวถึง เชื้อชาติ กำเนิด และการใช้ชีวิต',
        5: 'ข้อความที่กล่าวถึงสติปัญญา และความฉลาด',
        6: 'ข้อความที่มีการใช้ถ้อยคำรุนแรง การข่มขู่'
    }

    api_key = get_api_key()
    headers = {'Apikey':api_key, 'X-lib':PACKAGE_NAME}
    url = "https://api.aiforthai.in.th/bully"
    data = {'text':text}

    res = requests.post(url, data=data, headers=headers)
    if return_json == False:
        ids = res.json()['bully_type']
        if type(ids) == list:
            return {ids[0]:map_classes[ids[0]]}
        return {ids:map_classes[ids]}
    else:
        return res.json()
