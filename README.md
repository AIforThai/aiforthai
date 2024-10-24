# aiforthai
# Installation

```bash
pip install git+https://github.com/AIforThai/aiforthai.git
```

# How To Use

```bash
from aift import setting

setting.set_api_key('YOUR_API_KEY')
```
# Use case
## NLP
### Tokenizer
```bash
from aift.nlp import tokenizer

tokenizer.tokenize('สวัสดี AI')
```
```bash
tokenizer.tokenize('สวัสดี AI', return_json=True)
```
```bash
tokenizer.tokenize('สวัสดี AI', engine='trexplusplus') # engine = lexto, trexplus, trexplusplus
```
### Sentiment
```bash
from aift.nlp import sentiment

sentiment.analyze('อาหารร้านนี้อร่อยมาก') # engine = ssense, emonews, thaimoji, cyberbully
```
```bash
sentiment.analyze('อาหารร้านนี้อร่อยมาก', engine='emonews')
```
```bash
sentiment.analyze('อาหารร้านนี้อร่อยมาก', engine='thaimoji')
```
```bash
sentiment.analyze('อาหารร้านนี้อร่อยมาก', engine='cyberbully')
```
### Summarize
```bash
from aift.nlp import text_sum

text = """
ข้าว เป็นเมล็ดของพืชหญ้า Oryza sativa (ชื่อสามัญ: ข้าวเอเชีย) ที่พบมากในทวีปเอเชีย ข้าวเป็นธัญพืชซึ่งประชากรโลกบริโภคเป็นอาหารสำคัญ 
โดยเฉพาะอย่างยิ่งในทวีปเอเชีย จากข้อมูลเมื่อปี 2553 ข้าวเป็นธัญพืชซึ่งมีการปลูกมากที่สุดเป็นอันดับสามทั่วโลก รองจากข้าวสาลีและข้าวโพด 
ข้าวเป็นธัญพืชสำคัญที่สุดในด้านโภชนาการและการได้รับแคลอรีของมนุษย์ เพราะข้าวโพดส่วนใหญ่ปลูกเพื่อจุดประสงค์อื่น มิใช่ให้มนุษย์บริโภค ทั้งนี้ 
ข้าวคิดเป็นพลังงานกว่าหนึ่งในห้าที่มนุษย์ทั่วโลกบริโภค หลักฐานพันธุศาสตร์แสดงว่าข้าวมาจากการนำมาปลูกเมื่อราว 8,200–13,500 ปีก่อน ในภูมิภาคหุบแม่น้ำจูเจียงของจีน 
ก่อนหน้านี้ หลักฐานโบราณคดีเสนอว่า ข้าวมีการนำมาปลูกในเขตหุบแม่น้ำแยงซีในจีน ข้าวแพร่กระจายจากเอเชียตะวันออกไปยังเอเชียตะวันออกเฉียงใต้และเอเชียใต้ 
ข้าวถูกนำมายังทวีปยุโรปผ่านเอเชียตะวันตก และทวีปอเมริกาผ่านการยึดอาณานิคมของยุโรป[3] ปกติการปลูกข้าวเป็นแบบปีต่อปี ทว่าในเขตร้อน ข้าวสามารถมีชีวิตอยู่ได้หลายปีและสามารถไว้ตอ 
(ratoon) ได้นานถึง 30 ปี ต้นข้าวสามารถโตได้ถึง 1–1.8 เมตร ขึ้นอยู่กับพันธุ์และความอุดมสมบูรณ์ของดินเป็นหลัก มีใบเรียว ยาว 50-100 เซนติเมตร และกว้าง 2-2.5 เซนติเมตร 
ช่อดอกห้อยยาว 30-50 เซนติเมตร เมล็ดกินได้เป็นผลธัญพืชยาว 5-12 มิลลิเมตร และหนา 2-3 มิลลิเมตร 
การเตรียมดินสำหรับเพาะปลูกข้าวเหมาะกับประเทศและภูมิภาคที่ค่าแรงต่ำและฝนตกมาก 
เนื่องจากมันใช้แรงงานมากที่จะเตรียมดินและต้องการน้ำเพียงพอ อย่างไรก็ตาม ข้าวสามารถโตได้เกือบทุกที่ 
แม้บนเนินชันหรือเขตภูเขาที่ใช้ระบบควบคุมน้ำแบบขั้นบันได แม้ว่าสปีชีส์บุพการีของมันเป็นสิ่งพื้นเมืองของเอเชียและส่วนที่แน่นอนของแอฟริกา 
ร้อยปีของการค้าขายและการส่งออกทำให้มันสามัญในหลายวัฒนธรรมทั่วโลก วิธีแบบดั้งเดิมสำหรับเตรียมดินสำหรับข้าวคือทำให้น้ำท่วมแปลงชั่วขณะหนึ่งหรือหลังจากการตั้งของต้นกล้าอายุน้อย 
วิธีเรียบง่ายนี้ต้องการการวางแผนที่แข็งแรงและการให้บริการของเขื่อนและร่องน้ำ แต่ลดพัฒนาการของเมล็ดที่ไม่ค่อยแข็งแรงและวัชพืชที่ไม่มีภาวะเติบโตขณะจมน้ำ และยับยั้งศัตรูพืช 
ขณะที่การทำให้น้ำท่วมไม่จำเป็นสำหรับการเตรียมดินสำหรับเพาะปลูกข้าว 
วิธีทั้งหมดในการชลประทานต้องการความพยายามสูงกว่าในการควบคุมวัชพืชและศัตรูพืชระหว่างช่วงเวลาการเจริญเติบโตและวิธีที่แตกต่างสำหรับใส่ปุ๋ยลงดิน
"""

text_sum.summarize(text)
```
### Similarity
```bash
from aift.nlp import similarity

similarity.similarity('ต้มยำกุ้ง') # engine = thaiwordsim, wordapprox
```
```bash
similarity.similarity('ต้มยำกุ้ง', engine='thaiwordsim', model='thwiki') # model = thwiki, twitter
```
```bash
similarity.similarity('ต้มยำกุง', engine='wordapprox', model='food', return_json=True) # model = personname, royin, food
```
### Soundex
```bash
from aift.nlp import soundex

soundex.analyze('สมใจ') # model = personname, royin
```
### Grapheme to Phoneme
```bash
from aift.nlp import g2p

g2p.analyze('พนักงานโรงแรม XYZ ให้บริการต้อนรับดีมากกก')
```
### NER
```bash
from aift.nlp import ner

ner.analyze('งานประชุมวิชาการ สวทช. จัดขึ้นในวันที่ 25 มี.ค. พ.ศ. 2562 ณ อุทยานวิทยาศาสตร์ประเทศไทย')
```
### Question Answering
```bash
from aift.nlp import qa

qa.analyze("ยื่นประมูลรายเดียวทำไง", return_json=True)
```
### Tag Suggestion
```bash
from aift.nlp import tag

tag.analyze('ข้าวและแป้งมีสารอาหารหลักคือคาร์โบไฮเดรต', numtag=5)
```
### Text Cleansing
```bash
from aift.nlp import text_cleansing

text_cleansing.clean('เเพง')
```
### Translation
```bash
from aift.nlp import translation

translation.translate('สวัสดี', src='th', to='zh')
```
```bash
translation.translate('你好', src='zh', to='th')
```
## Speech
### Text to Speech
```bash
from aift.speech import tts

tts.convert('สวัสดีครับ', 'test.wav')
```
### Speech to Text
```bash
from aift.speech import stt

stt.convert('test.wav', return_json=True)
```
## Image
### Car Logo
```bash
from aift.image import carlogo

carlogo.analyze('image.png',  return_json=True)
```
### Thai Food
```bash
from aift.image import thaifood

thaifood.analyze('image.png')
```
### Thai License Plate Recognition
```bash
from aift.image import lpr

lpr.analyze('image.png', crop=0, rotate=1)
```
### Hand Written
```bash
from aift.image import handwritten

handwritten.analyze('image.png')
```
### NSFW
```bash
from aift.image import nsfw

nsfw.analyze('image.png')
```
### Face Detection
```bash
from aift.image import detection

detection.analyze('image.png') # engine = face, facemask
```
```bash
detection.analyze('image.png', engine='facemask')
```