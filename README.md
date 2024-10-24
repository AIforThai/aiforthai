# AIFT an AI for Thai Python Package.

#### Contributor: 
Piyawat Chuangkrud
# Installation

```bash
pip install aift
```

# How To Use

```python
from aift import setting

setting.set_api_key('YOUR_API_KEY')
```
# Use Case
## Multimodal
#### TextQA
```python
from aift.multimodal import textqa

textqa.generate('ข้อความ')
```
#### AudioQA
```python
from aift.multimodal import audioqa

audioqa.generate('audio.mp3', 'ถอดเสียงข้อความ')
```
#### VQA
```python
from aift.multimodal import vqa

vqa.generate('image.jpg', 'บรรยายรูปนี้')
```

## NLP
### Alignment
#### EN Alignment
```python
from aift.nlp.alignment import en_alignment

en_alignment.analyze("en_text", 'th_text', return_json=True)
```
#### ZH Alignment
```python
from aift.nlp.alignment import zh_alignment

zh_alignment.analyze("zh_text", 'th_text')
```
### Grapheme to Phoneme
#### G2P
```python
from aift.nlp import g2p

g2p.analyze('ข้อความ')
```
### longan
#### Sentence Token
```python
from aift.nlp.longan import sentence_tokenizer

sentence_tokenizer.tokenize('ข้อความ')
```
#### Tagger
```python
from aift.nlp.longan import tagger

tagger.tag('ระบุ|ข้อความ|ใน|นี้')
```
#### Token Tagger
```python
from aift.nlp.longan import token_tagger

token_tagger.tokenize_tag('ข้อความ')
```
#### Tokenizer
```python
from aift.nlp.longan import tokenizer

tokenizer.tokenize('ข้อความ')
```
### Name Entity Recognition
#### example
```python
from aift.nlp import ner

ner.analyze('ข้อความ')
```
### Question Answering
#### example
```python
from aift.nlp import qa

qa.analyze('ข้อความ')
```
### Sentiment Analysis
#### example
```python
from aift.nlp import sentiment

sentiment.analyze('ข้อความ') # engine = ssense, emonews, thaimoji, cyberbully
```
```python
sentiment.analyze('ข้อความ', engine='emonews')
```
```python
sentiment.analyze('ข้อความ', engine='thaimoji')
```
```python
sentiment.analyze('ข้อความ', engine='cyberbully')
```
### Similarity
#### example
```python
from aift.nlp import similarity

similarity.similarity('ข้อความ') # engine = thaiwordsim, wordapprox
```
```python
similarity.similarity('ข้อความ', engine='thaiwordsim', model='thwiki') # model = thwiki, twitter
```
```python
similarity.similarity('ข้อความ', engine='wordapprox', model='food', return_json=True) # model = personname, royin, food
```
### Soundex
#### example
```python
from aift.nlp import soundex

soundex.analyze('ชื่อ') # model = personname, royin
```
### Tag Suggestion
#### example
```python
from aift.nlp import tag

tag.analyze('ข้อความ', numtag=5)
```
### Text Cleansing
#### example
```python
from aift.nlp import text_cleansing

text_cleansing.clean('ข้อความ')
```
### Text Summarization
#### example
```python
from aift.nlp import text_sum

text = """
long text
"""

text_sum.summarize(text)
```
### Tokenizer
#### example
```python
from aift.nlp import tokenizer

tokenizer.tokenize('ข้อความ')
```
```python
tokenizer.tokenize('ข้อความ', return_json=True)
```
```python
tokenizer.tokenize('ข้อความ', engine='trexplusplus') # engine = lexto, trexplus, trexplusplus
```
### Translation
#### EN-TH
```python
from aift.nlp.translation import en2th

en2th.translate("en_text")
```
#### TH-EN
```python
from aift.nlp.translation import th2en

th2en.translate("ข้อความ")
```
#### ZH-TH, TH-ZH
```python
zh_translate.translate('ข้อความ', src='th', to='zh', return_json=True)
```
```python
zh_translate.translate('zh_text', src='zh', to='th', return_json=True)
```

## IMAGE
### Classification
#### Chest X-Ray Classification
```python
from aift.image.classification import chest_classification

chest_classification.analyze('image.jpg', return_json=True)
```
#### Mask Detection
```python
from aift.image.classification import maskdetection

maskdetection.analyze('image.jpg')
```
#### NSFW
```python
from aift.image.classification import nsfw

nsfw.analyze('image.jpg')
```
#### Violence Classification
```python
from aift.image.classification import violence_classification

violence_classification.analyze('image.jpg')
```

### Correlator
#### Correlator
```python
from aift.image.correlator import correlator

correlator.analyze('image.jpg', arr='คน', num=1)
```
### Detection
#### Carlogo
```python
from aift.image.detection import carlogo

carlogo.analyze('image.jpg',  return_json=True)
```
#### Face Blur
```python
from aift.image.detection import face_blur

face_blur.analyze('image.jpg')
```
#### Face Detection
```python
from aift.image.detection import face_detection

face_detection.analyze('image.jpg', return_json=True)
```
#### Handwritten
```python
from aift.image.detection import handwritten

handwritten.analyze('image.jpg')
```
#### Thai License Plate Recognition
```python
from aift.image.detection import lpr

lpr.analyze('image.jpg', crop=0, rotate=1)
```
#### Weapon Detection
```python
from aift.image.detection import weapon_detection

weapon_detection.analyze('image.jpg')
```
### Dicom to Image
#### Dicom2image
```python
from aift.image.dicom2image import dicom2image

dicom2image.analyze('image.dcm')
```
### Super Resolution
#### Super Resolution
```python
from aift.image import super_resolution

super_resolution.analyze('image.jpg')
```
### Thai Food
#### Thai Food
```python
from aift.image import thaifood

thaifood.analyze('image.jpg')
```

## SPEECH
#### Text to Speech
```python
from aift.speech import tts

tts.convert('สวัสดีครับ', 'file.wav')
```
#### Speech to Text
```python
from aift.speech import stt

stt.convert('file.wav', return_json=True)
```
