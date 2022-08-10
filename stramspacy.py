import streamlit as st
import spacy
import spacy_streamlit
import numpy as np
import PIL
import easyocr
import matplotlib.pyplot as plt

from PIL import Image,ImageDraw
from spacy import displacy

image11 = Image.open('pipesegm.png')
path_pict = '/app/easyocrstream/pictures/'

st.subheader('Распознавание документов с помощью EasyOCR.')
st.write("""
Лабораторная работа *"Распознавание документов с помощью библиотеки [EasyOCR](https://www.jaided.ai/easyocr/)"* позволяет продемонстрировать 
работу фреймворка, основанного на [Pytorch](https://pytorch.org/)  для извлечения текста из изображения. Это обычная OCR библиотека, которая может читать как
текст с большим расстоянием между строк, так и плотный текст в документе. В настоящее время поддерживает более 80 языков и расширяется.
""")

with st.expander("Общая схема"):
  st.image(image11)
  st.markdown(
    '''
    \n**Этапы:**
    \n1. База данных типовых договоров:
    \nСодержит более 100 текстовых файлов типовых договоров купли, продажи, аренды, размещения вклада, банковского обслуживания и т.д.
    \n2. Библиотека слоев:
    \nСодержит набор слоев, используемых нейронной сетью.  [tensorflow](https://www.tensorflow.org/).
    \n3. Настройка модели:
    \nУстанавливается тип и количество слоев, а также количество нейронов в них.
    \n4. Обучение модели:
    \nВо время этого процесса нейросеть читает документы и обучается их воспроизводить.
    \n5. Проверка точности:
    \nНа этом этапе программист проверяет работу сети с помощью тестовых документов.
    \n6. Функция обработки текстового документа:
    \nПреобразует документ, который выдает нейронная сеть, в понятный для человека вид.
    \n7. Загрузка документа из нескольких предложенных:
    \nНа выбор студенту предлагается пять документов, которые можно отправить в нейронную сеть на обработку. В результате получается документ с выделенными цветными параграфами.
    \n8. Приложение Streamlit:
    \nОтображение документа.
    ''')

st.write('Нейронная сеть, представленная здесь, обучена распзнавать документы в виде JPG файлов.')
st.write('Вы можете выбрать любой документ из представленных в списке для распознавания.')
option1 = st.selectbox('Какой документ Вы выбираете?',('ИНН','СНИЛС','полис омс','паспорт1','паспорт2'))
col1,col2 = st.columns(2)
with col1:
    img_name = path_pict + option1 + '.jpg'
    img = plt.imread(img_name)
    st.image(img)
with col2:
    #text1 = pytesseract.image_to_string(img_name, lang='rus').replace('\n\x0c', '')
    #data1 = pytesseract.image_to_data(img_name, output_type=Output.DICT)
    #st.write(text1)
    reader1 = easyocr.Reader(['ru'])
    bounds1 = reader1.readtext(img_name)
    image2 = boxesdrawer.draw_boxes(img,bounds1)
    image2.save('outfile1.jpg')
    st.image(image2)
