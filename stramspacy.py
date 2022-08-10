import streamlit as st

import spacy
from spacy import displacy

import spacy_streamlit

st.subheader('Распознавание документов с помощью EasyOCR.')
st.write("""
Лабораторная работа *"Распознавание документов с помощью библиотеки EasyOCR"* позволяет продемонстрировать 
работу фреймворка, основанного на LSTM(Long-Short-Term-Memory) нейронной сети,
 обученной распознавать печатный текст документов. Подробнее про LSTM слои можно почитать здесь https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM .
""")
