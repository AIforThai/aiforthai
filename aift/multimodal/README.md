# PATHUMMA LLM
Pathumma LLM is a friendly and an easy to use multimodals python lib. Simply call the `generate` function with the relevant input, such as a prompt or a related audio or image file.

#### Contributor: 
Piyawat Chuangkrud

## INSTALLATION
```sh
pip install aift
```

## TEXT LLM

### params
The `generate` function designing for single-turn conversation. It has the following parameters:

* **instruction** (str: `required`): The prompt text for the model.
* **system_prompt** (str): The system prompt to define the model's behavior.
* **max_new_tokens** (int): The maximum number of tokens to generate (default=512).
* **temperature** (float): Controls the randomness of the generated text (default=0.4).
* **return_json** (bool): Determines the response format. If True, the response is in JSON format; otherwise, it's in plain text (default=True).

_NOTE:_ 
A higher temperature value (e.g., 0.9) will result in more creative and diverse outputs, but they may be less relevant to the prompt. A lower temperature value (e.g., 0.2) will produce more focused and deterministic outputs


### example
```python
# import package and set API_KEY
from aift.multimodal import textqa
from aift import setting
setting.set_api_key('YOUR_API_KEY')

# response in plain text format
# The "instruction" parameter can be omitted if it's in the first position
textqa.generate('คุณคือใคร', return_json=False)
# output
# 'ฉันเป็น AI ที่สร้างขขึ้นโดย NECTEC ฉันชชื่อ Pathumma LLM และฉันพร้อมทที่จะช่วยเหลือคุณ'


# response in json format
textqa.generate(instruction='1+1')
# output
# {'instruction': '1+1', 'system_prompt': 'You are Pathumma LLM, created by NECTEC (National Electronics and Computer Technology Center). Your are a helpful assistant.', 'content': '2', 'temperature': 0.4, 'max_new_tokens' : 256, 'execution_time': '0.04'}
```

### params
The `chat` function designing for multi-turn or conversation. It has the following parameters:

* **instruction** (str: `required`): The prompt text for the model.
* **sessionid** (str: `required`): A unique identifier for the user's session to track conversation history.
* **context** (str): Initial context for the conversation (1,000 characters max)
* **temperature** (float): Controls the randomness of the generated text (default=0.4).
* **return_json** (bool): Determines the response format. If True, the response is in JSON format; otherwise, it's in plain text (default=True).

_NOTE:_ 
A higher temperature value (e.g., 0.9) will result in more creative and diverse outputs, but they may be less relevant to the prompt. A lower temperature value (e.g., 0.2) will produce more focused and deterministic outputs


### example
```python
# import package and set API_KEY
from aift.multimodal import textqa
from aift import setting
setting.set_api_key('YOUR_API_KEY')

# response in plain text format
# The "instruction" parameter can be omitted if it's in the first position
context = 'ขณะนี้มีเงิน 100 บาท'
textqa.chat('ตอนนี้มีเงินเท่าไหร่', sessionid='YOUR_SESSION', context=context, temperature=0.2, return_json=False)
# output
# 'ขณะนี้มีเงิน 100 บาท'

textqa.chat('ซื้อขนมไป 20 เหลือเงินเท่าไหร่', sessionid='YOUR_SESSION', context=context, temperature=0.2, return_json=False)
# output
# 'ขณะนี้มีเงิน 80 บาท'

textqa.chat('ให้เงินน้อง 15 บาท เหลือเงินเท่าไหร่', sessionid='YOUR_SESSION', context=context, temperature=0.2, return_json=False)
# output
# 'ขณะนี้มีเงิน 65 บาท'
```
---

---

## AUDIO LLM
### params
the `generate` function has the following parameters:

* **file** (str: `required`): File path to the audio file. Supported formats: .wav, .mp3.
* **instruction** (str: `required`): Text prompt for the model. Examples: transcription, sentiment analysis, speaker gender identification, or QA related to the audio content.

### example
```python
# import package and set API_KEY
from aift.multimodal import audioqa
from aift import setting
setting.set_api_key('YOUR_API_KEY')

audioqa.generate('/path/to/your/audio_file.mp3', 'แปลข้อความ')
# output
# {'filename': '/path/to/your/audio_file.mp3',
#  'content_type': 'audio/mpeg',
#  'prompt': 'แปลข้อความ',
#  'content': ['วันนั้น เห็น พรี แอป ของ พิพิธภัณฑ์ ศิลปะ ว่า มี งาน จัด แสดง ชุด ใหม่ เข้ามา แล้ว เกี่ยวกับ ภาพพิมพ์ ญี่ปุ่น แฟน เร นี่ ชอบ มาก'],
#  'execute_time': '2.93'}
```
---

## VISION LLM
the `generate` function has the following parameters:

* **file** (str: `required`): File path to the image file. Supported formats: .jpg, .png.
* **instruction** (str: `required`): A text prompt to instruct the model, such as image captioning or vision QA.

### example
```python
# import package and set API_KEY
from aift.multimodal import vqa
from aift import setting
setting.set_api_key('YOUR_API_KEY')

vqa.generate('/path/to/your/image_file/car-demo.png', 'รูปนี้คืออะไร')
# output
# {'filename': '/path/to/your/image_file/car-demo.png',
#  'content_type': 'image/jpeg',
#  'query': 'รูปนี้คืออะไร',
#  'content': 'รถยนต์คันสีแดงจอดอยู่ข้างกับกำแพงสีขาวมีลายเส้นสีน้ำตาล',
#  'execution_time': '1.29'}
```
