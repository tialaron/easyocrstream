import streamlit as st
import spacy
import spacy_streamlit
import numpy as np
import PIL
import easyocr
import matplotlib.pyplot as plt
import cv2

from PIL import Image,ImageDraw
from spacy import displacy

image11 = Image.open('pipesegm.png')
path_pict = '/app/easyocrstream/pictures/'

st.markdown('''<h1 style='text-align: center; color: #F64A46;'
            >Распознавание документов с помощью EasyOCR.</h1>''', 
            unsafe_allow_html=True)

st.write("""
Лабораторная работа *"Распознавание документов с помощью библиотеки [EasyOCR](https://www.jaided.ai/easyocr/)"* позволяет продемонстрировать 
работу фреймворка, основанного на [Pytorch](https://pytorch.org/)  для извлечения текста из изображения. Это обычная [OCR](https://en.wikipedia.org/wiki/Optical_character_recognition) библиотека, которая может читать как
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
st.markdown('''<h1 style='text-align: center; color: black;'
            >Задача лабораторной работы.</h1>''', 
            unsafe_allow_html=True)
st.write('Нейронная сеть, представленная здесь, обучена распзнавать документы в виде JPG файлов.')
st.write('Вы можете выбрать любой документ из представленных в списке для распознавания.')
option1 = st.selectbox('Какой документ Вы выбираете?',('ИНН','СНИЛС','полис омс','паспорт1','паспорт2'))
full_path = path_pict+option1+'_ЧБ.jpg'
img = Image.open(full_path)
st.image(full_path)
st.write('Теперь нужно разметить документ таким образом, чтобы выделить из него текст.')
st.write('Для этого нажмите на кнопку "Распознать" и дождитесь когда появится документ с выделенными участками текста')
is_clicked1 = st.button("Распознать")
if is_clicked1:
            image1 = open(full_path,'rb')
            f = image1.read()
            file_bytes = np.asarray(bytearray(f),dtype=np.uint8)
            bytearray_img = cv2.imdecode(file_bytes, 1)
            image1.close()
            reader1 = easyocr.Reader(['ru'])
            bounds = reader1.readtext(bytearray_img)
            print(bounds)
            image2 = boxesdrawer.draw_boxes(path_img, bounds)
            image2.save('out111.jpg')
            st.image('out111.jpg')
            
            
