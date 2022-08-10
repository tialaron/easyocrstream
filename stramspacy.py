import streamlit as st
import spacy
import spacy_streamlit
import numpy as np
import PIL

from spacy import displacy


st.subheader('Распознавание документов с помощью EasyOCR.')
st.write("""
Лабораторная работа *"Распознавание документов с помощью библиотеки EasyOCR"* позволяет продемонстрировать 
работу фреймворка, основанного на LSTM(Long-Short-Term-Memory) нейронной сети,
 обученной распознавать печатный текст документов. Подробнее про LSTM слои можно почитать здесь https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM .
""")
